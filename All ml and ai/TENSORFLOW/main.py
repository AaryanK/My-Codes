
from pyexpat import features
import pandas as pd
import tensorflow as tf







data = pd.read_csv("car.data")


def train_test_split(data,test_size=0.2):
    test_size = int(len(data)*test_size)
    train_size =int(len(data)-test_size)
    return data[:train_size],data[train_size:]

x_train,x_test = train_test_split(data)
y_train,y_test = x_train.pop('class'),x_test.pop('class')

categories = ["buying","maint","door","persons","lug_boot","safety"]
y = ['class']


features = []
for feats in categories:
    vocs = x_train[feats].unique()
    features.append(tf.feature_column.categorical_column_with_vocabulary_list(feats,vocs))

print(features)


def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():  # inner function, this will be returned
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data and its label
    if shuffle:
      ds = ds.shuffle(1000)  # randomize order of data
    ds = ds.batch(batch_size).repeat(num_epochs)  # split dataset into batches of 32 and repeat process for number of epochs
    return ds  # return a batch of the dataset
  return input_function  # return a function object for use

train_input_fn = make_input_fn(x_train, y_train)  # here we will call the input_function that was returned to us to get a dataset object we can feed to the model
eval_input_fn = make_input_fn(x_test,y_test, num_epochs=1, shuffle=False)

linear_est = tf.estimator.LinearClassifier(feature_columns=features)

linear_est.train(train_input_fn)  # train
result = linear_est.evaluate(eval_input_fn)  # get model metrics/stats by testing on tetsing data

print(result['accuracy']) 