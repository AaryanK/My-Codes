import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing


df = pd.read_csv('indian_food.csv',sep=',')

le = preprocessing.LabelEncoder()
diet = le.fit_transform(list(df['diet']))
flavour = le.fit_transform(list(df['flavor_profile']))
state = le.fit_transform(list(df['state']))
region = le.fit_transform(list(df['region']))


predict = 'state'

x = list(zip(diet,region,state))
y = list(flavour)


x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)
acc = model.score(x_test,y_test)
print(acc)
#predicted = model.predict(x_test)

