import os

for i in range(len(os.listdir('train/cats'))):
    os.rename(f'train/cats/cat.{i}.jpg',f'train/cats/c{i}.jpg')
