from sklearn import datasets
import sklearn
from sklearn.neighbors import KNeighborsClassifier

df = datasets.load_sample_images()
x = df.images
y=[0,1]

clf = KNeighborsClassifier()
clf.fit(x,y)
ans = clf.predict(x[0])
print(ans,y[0])
