import pyscreenshot as ImageGrab 
import time
time.sleep(3)
# hit('up') 

while True:
    image = ImageGrab.grab().convert('L')  
    data = image.load()


    for i in range(185,245):
        for j in range(450,490):
            data[i, j] = 0
    image.show()
    break
