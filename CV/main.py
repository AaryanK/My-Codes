import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn import linear_model
import sklearn
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
import os


data = pd.read_csv('student-mat.csv',sep=';')
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]


predict = "G2"

X = np.array(data.drop([predict],1))
y = np.array(data[predict])

if os.path.exists('student.pickle'):
    pickle_in = open("student.pickle",'rb')
    linear = pickle.load(pickle_in)

    predictions = linear.predict(x_test)

    for x in range(len(predictions)):
        print('predicted :',int(predictions[x]), x_test[x],'actual :' ,y_test[x])

else:
    x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X, y,test_size=0.1)
    linear =linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    '''if accuracy > 0.85:
        with open("student.pickle",'wb')as f:
            pickle.dump(linear,f)'''
    predictions = linear.predict(x_test)

    for x in range(len(predictions)):
        print('predicted :',int(predictions[x]), x_test[x],'actual :' ,y_test[x])

