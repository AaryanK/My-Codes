import PIL
from tensorflow.keras.models import load_model
import numpy as np

model = load_model("student.model")

data = PIL.Image.open("train/face_0.jpg").resize((150,150))
data = np.array(data)/255
print(data.shape)
model.predict(data)