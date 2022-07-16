import nltk
import json
import random
import pickle 
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from tensorflow.keras.optimizers import SGD
import numpy as np

lemmatizer = WordNetLemmatizer()


intents = json.loads(open('intents.json').read())


words = []
classes = []
documents = []
ignores = ['\'','?','!','.','.']

for intent in intents['intents']:
	for pattern in intent['patterns']:
		wordlist = nltk.word_tokenize(pattern)
		words.extend(wordlist)
		documents.append((wordlist,intent['tag']))

		if intent['tag'] not in classes:
			classes.append(intent['tag'])
		
words = [lemmatizer.lemmatize(word) for word in words if word not in ignores]
words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words,open('words.pickle','wb'))
pickle.dump(classes,open('classes.pickle','wb'))

# training = []
# output_empty = [0]*len(classes)

# for document in documents:
# 	bag=[]
# 	word_patterns = document[0]
# 	word_patterns = [lemmatizer.lemmatize(word.lower())for word in word_patterns]
# 	for word in words:
# 		bag.append(1) if word in word_patterns else bag.append(0)

# 	output_row = list(output_empty)
# 	output_row[classes.index(document[1])] = 1
# 	training.append([bag,output_row])

# random.shuffle(trainin
# training = np.array(training)

# x_train = list(training[:,0])
# y_train = list(training[:,1])

# model = keras.Sequential()
# model.add(keras.layers.Dense(128,input_shape=(len(x_train[0]),),activation='relu'))
# model.add(keras.layers.Dropout(0.5))
# model.add(keras.layers.Dense(64,activation='relu'))
# model.add(keras.layers.Dropout(0.5))
# model.add(keras.layers.Dense(len(y_train[0]),activation='softmax'))

# optimizer = SGD(learning_rate=0.01,momentum=0.9,nesterov=True)
# model.compile(loss='categorical_crossentropy',optimizer=optimizer,metrics=['accuracy'])

# mod = model.fit(np.array(x_train),np.array(y_train),epochs=200,batch_size=5,verbose=1)
# model.save('chatbot_model.h5',mod)
# print('done')