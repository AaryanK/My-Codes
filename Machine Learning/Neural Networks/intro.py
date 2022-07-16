import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

df = keras.datasets.fashion_mnist
(x_train,y_train),(x_test,y_test)=df.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

x_train = x_train/255.0
x_test = x_test/255.0

# 

# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(28,28)),
#     keras.layers.Dense(128,activation="relu"),
#     keras.layers.Dense(10,activation="softmax")

# ])

# model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
# model.fit(x_train,y_train,epochs=15)
model = keras.models.load_model("model.aaryan")
loss,acc = model.evaluate(x_test,y_test)

print("Acc : ",acc)

predicted = model.predict(x_test)
# for i in range(len(predicted)):
    # print(f"Predicted : {class_names[np.argmax(predicted[i])]} {round(np.max(predicted[i])*100)} % \nActual :{class_names[y_test[i]]}")

dict = {}
dict["Predicted"] = []
dict["Accuracy"] = []
dict["Actual"] = []

for i in range(len(predicted)):
    dict["Predicted"].append(class_names[np.argmax(predicted[i])])
    dict["Accuracy"].append(f"{round(np.max(predicted[i])*100)}%")
    dict["Actual"].append(f"{class_names[y_test[i]]}")

import pandas
df = pandas.DataFrame(dict)
df.to_csv("Model.xlsx")