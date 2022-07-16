random.shuffle(training)
training = np.array(training)

x_train = list(training[:,0])
y_train = list(training[:,1])

model = keras.Sequential()
model.add(keras.layers.Dense(128,input_shape=(len(x_train[0]),),activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(64,activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(len(y_train[0]),activation='softmax'))

optimizer = SGD(learning_rate=0.01,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=optimizer,metrics=['accuracy'])

mod = model.fit(np.array(x_train),np.array(y_train),epochs=200,batch_size=5,verbose=1)
model.save('chatbot_model.h5',mod)
print('done')