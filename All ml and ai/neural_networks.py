import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data =keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)=data.load_data()
print(train_labels[6])

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


train_images = train_images/255.0
test_images = test_images/255.0


print(train_images)
print(test_images)

model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(28,28)),
                          keras.layers.Dense(128,activation='relu'),                     
                          keras.layers.Dense(10,activation='softmax')                     ])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(train_images,train_labels,epochs=9)

test_loss,test_acc=model.evaluate(test_images,test_labels)
print('accuracy: ',test_acc)

prediction = model.predict(test_images)
print(class_names[np.argmax(prediction[0])])

plt.figure(figsize=(5,5))
for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel('actual: '+class_names[test_labels[i]])
    plt.title('predicted: '+class_names[np.argmax(prediction[i])])
    plt.show()