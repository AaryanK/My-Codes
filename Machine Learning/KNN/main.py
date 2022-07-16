from numpy.testing._private.utils import KnownFailureException
from sklearn import datasets
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

features = iris.data
labels = iris.target
descr = iris.DESCR


df = pd.DataFrame(iris.data)
df.columns = ["sepal length","sepal width","petal length","petal width"]
label = ["Iris Setosa",
        "Iris Versicolour",
        "Iris Virginica"]

clf = KNeighborsClassifier()
clf.fit(features,labels)
print(f"Accuracy is : {clf.score(features,labels)*100}%")
predict = clf.predict([[1,1,1,1]])
print(f"Prediction : {label[int(predict)]}")


import matplotlib.pyplot as plot

plot.scatter(df["sepal length"],df["sepal width"])
plot.scatter(df["petal length"],df["petal width"])
plot.show()