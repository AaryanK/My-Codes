
from matplotlib import pyplot as plt
from pdf2image import convert_from_path
import numpy as np
import os

count = 0
for i in os.listdir('download_papers'):
    images = convert_from_path(f'download_papers/{i}') #Read pdf file
    images = images[1:]

    for j in images:
        plt.imsave(f"papers/{count}.jpg",np.array(j))
        count+=1


