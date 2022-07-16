from math import pi
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


data = pd.read_csv('student-mat.csv',sep=";")


data = data[["G1","G2","G3"]]

predict="G3"

X=np.array(data[["G1","G2"]])
y = np.array(data[predict])

# acc=0.1
# while acc<0.9:
#     x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X,y,test_size=.4)
#     model = linear_model.LinearRegression()


#     model.fit(x_train,y_train)
#     acc = model.score(x_test,y_test)
#     print(acc)
# import pickle
# filename = 'finalized_model.aaryan'
# pickle.dump(model, open(filename, 'wb'))


# x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X,y,test_size=.99)

def predictor(g1,g2):
    ans = model.predict([[g1,g2]])
    return round(ans[0])


import pickle
filename = 'finalized_model.aaryan'
# pickle.dump(model, open(filename, 'wb'))
model = pickle.load(open(filename, 'rb'))
def model():
    return model
