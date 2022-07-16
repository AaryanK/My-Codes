import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn import linear_model
import sklearn
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
import os



df = pd.read_csv('winequality-red.csv',sep=';')

df = df[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides',"free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]]

tbp = 'quality'

X = np.array(df.drop([tbp],1))
y = np.array(df[tbp])

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X, y,test_size=0.1)
linear =linear_model.LinearRegression()
linear.fit(x_train, y_train)
accuracy = linear.score(x_test, y_test)
print(accuracy)