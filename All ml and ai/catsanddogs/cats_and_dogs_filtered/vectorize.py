from PIL import Image
import numpy as np
'''import tensorflow as tf
from tensorflow import keras'''
import os



def give_data(dir):
  array = np.empty((1000,300),dtype=np.uint8)
  for i in dir:
    animal = Image.open(f'{dir}/{i}').resize(300,300)
    animal = np(animal)
    array.append(animal)
  return array


'''
def load_training_and_testing_data():
  cat_train_array = np.array(dtype=np.uint8)
  dog_train_array = np.array(dtype=np.uint8)
  cat_test_array = np.array(dtype=np.uint8)
  dog_test_array = np.array(dtype=np.uint8)

  train = 'cats_and_dogs_filtered/train'
  train_data = os.listdir('cats_and_dogs_filtered/train')
  cat_train = os.listdir(f'{train}/{train_data[0]}')
  dog_train = os.listdir(f'{train}/{train_data[1]}')
  test = f'cats_and_dogs_filtered/validation'
  cat_test =os.listdir(f'{test}/cats')
  dog_test =os.listdir(f'{test}/dogs')

  for i in cat_train:
    cat = open(i)
    cat_train_array.append(np(cat))
  for i in dog_train:
    cat = open(i)
    dog_train_array.append(np(cat))  

  for i in cat_test:
    cat = open(i)
    cat_test_array.append(np(cat))
  for i in dog_test:
    cat = open(i)
    dog_test_array.append(np(cat))  


  x_train=cat_train_array
  y_train=dog_train_array
  x_test=cat_test_array
  y_test=dog_test_array

  return(x_train,_y_train),(x_test,y_test)'''


# print(load_training_and_testing_data()[0][0])



# (x_train,y_train),(x_test,y_test)

print(give_data(os.listdir('train/cats')))
