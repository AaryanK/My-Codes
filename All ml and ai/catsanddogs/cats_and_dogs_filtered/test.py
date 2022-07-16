from PIL import Image
import numpy as np
import os

def give_data(dir):
    array = np.empty((1000,300),dtype=np.uint8)
    i=1
    animal = Image.open(f'{dir}/{i}').resize(300,300)
    animal = np(animal)
    array.append(animal)
    return array
print(give_data(os.listdir('train/cats')))
