from sklearn.model_selection import train_test_split
import torch
import numpy as np
import matplotlib.pyplot as plt
import torch.nn as nn
import pandas as pd

df = pd.read_csv('student-mat.csv',sep=';')
df = df[['G1', 'G2', 'G3']]

features = np.array(df.drop('G3', axis=1))
labels = np.array(df['G3'])

X_train,X_test,Y_train, Y_test = train_test_split(features,labels, test_size=0.4)
# print(len(X_train),len(Y_train))

#Initialization
X = torch.from_numpy(X_train).float()
Y = torch.from_numpy(Y_train).float()
# print(X)
# print(Y)

n_samples,n_features = X.shape
input_size =n_features
output_size = 1
model = nn.Linear(input_size,output_size)


#Loss Function
criterion = nn.MSELoss()
optimizer  = torch.optim.SGD(model.parameters(),lr=0.001)


epochs = 1000
for epoch in range(epochs):
    y_predicted = model(X)
    loss = criterion(y_predicted,Y)
    print(f'epoch {epoch+1}/{epochs} loss {loss.item()}')
    
    loss.backward()#Back Propagation
    optimizer.step()#Update m and B values
    optimizer.zero_grad()


#Testing
X_test = torch.from_numpy(X_test).float()
Y_test = torch.from_numpy(Y_test).float()


ax = plt.axes(projection="3d")
ax.scatter(X_test.transpose(0,1)[0],X_test.transpose(0,1)[0],Y_test,color='red')
y_predicted = model(X_test)
predicted = y_predicted.detach().numpy()
# print(predicted.transpose()[0].shape)
ax.plot(X_test.transpose(0,1)[0],X_test.transpose(0,1)[0],predicted.transpose()[0],color='blue')
plt.show()