# from nltk.tokenize import sent_tokenize
import numpy as np
import json
from nltk.stem import WordNetLemmatizer
import nltk
import random
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import SGD



lemmatizer = WordNetLemmatizer()


words = []
cats = []
docs = []

ignores = ['?',',','.','(',')',';',':','','`','’']

intents = json.loads(open('intents.json').read())

for intent in intents['main_intents']:
    for pattern in intent['patterns']:
        wlist = nltk.word_tokenize(pattern)
        words.extend(wlist)
        docs.append((wlist,intent['cat']))

        if intent['cat'] not in cats:
            cats.append(intent['cat'])


words = [lemmatizer.lemmatize(word) for word in words if word not in ignores]
words = sorted(set(words))
print(len(words))
import pickle

pickle.dump(words,open('words.pickle','wb'))
pickle.dump(cats,open('classes.pickle','wb'))

output_empty = [0]*len(cats)
training = []

for doc in docs:
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        if word in word_patterns:
            bag.append(1)
        else:
            bag.append(0)
    output_row = list(output_empty)
    output_row[cats.index(doc[1])] = 1
    training.append([bag,output_row])

random.shuffle(training)

training = np.array(training)

x_train = list(training[:,0])
y_train = list(training[:,1])

model = Sequential()
model.add(Dense(128,input_shape=(len(x_train[0]),),activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(y_train[0]),activation='softmax'))


sgd = SGD(learning_rate=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
mod = model.fit(np.array(x_train),np.array(y_train),epochs=10,batch_size=5,verbose=1)
model.save('model.h5',mod)