import numpy as np
import os
from PIL import Image
import tensorflow as tf
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
# from tensorflow.keras.optimizers import SGD
from keras.layers import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K


from keras.models import Sequential
from keras.layers import Dense



train_data_dir = "train/"

a = np.array([np.array(Image.open(train_data_dir+i).resize((150,150))) for i in os.listdir(train_data_dir)])/255


x_train = a
y_train = np.array([1]*x_train.shape[0])



model = Sequential()
model.add(Flatten())
model.add(Dense(16, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation = 'softmax'))


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)
model.save("student.model")