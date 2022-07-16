import json
import nltk
import numpy as np
import random
from tensorflow import keras
from tensorflow.keras.optimizers import SGD


intents = json.load(open('intents.json'))


category = []
training_data = []
total_words = []

for i in intents['intents']:

    category.append(i['tag']) if i['tag'] not in category else None
    for j in i['patterns']:
        total_words.extend(nltk.tokenize.word_tokenize(j))

 
total_words = sorted(set(total_words))

input_empty = [0]*len(total_words)



for i in intents['intents']:
    for j in i['patterns']:
        
        words = nltk.tokenize.word_tokenize(j)
        input_d=[0]*len(total_words)
        for word in words:
            input_d[total_words.index(word)] = 1
        tag_empty = [0]*len(category)
        tag_empty[category.index(i['tag'])] = 1

            
                

        training_data.append([input_d, tag_empty])



for i in training_data:
    final = ""
    for j in range(len(i[0])):
    
        if i[0][j] == 1:
            final+=total_words[j]
            

random.shuffle(training_data)
training_data = np.array(training_data)
x = list(training_data[:,0])
y = list(training_data[:,1])


model = keras.Sequential()
model.add(keras.layers.Dense(128,input_shape=(len(x[0]),),activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(64,activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(len(y[0]),activation='softmax'))

optimizer = SGD(learning_rate=0.01,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=optimizer,metrics=['accuracy'])
mod = model.fit(np.array(x),np.array(y),epochs=10,batch_size=5,verbose=1)
model.save('chatbot_model.h5',mod)
print('done')


            







    