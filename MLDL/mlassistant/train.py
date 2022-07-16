import nltk
import json
import random
import pickle 
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from tensorflow.keras.optimizers import SGD
import numpy as np
from tensorflow.keras.models import load_model


lemmatizer = WordNetLemmatizer()

def save_model():
    intents = json.loads(open('intents.json').read())

    nltk.download('wordnet')
    nltk.download('punkt')

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

    training = []
    output_empty = [0]*len(classes)
    # print(output_empty)
    print(len(documents))
    print(documents)
    print(words)

    print(len(words))
    for document in documents:
        bag=[]
        word_patterns = document[0]
        word_patterns = [lemmatizer.lemmatize(word.lower())for word in word_patterns]
        for word in words:
            bag.append(1) if word in word_patterns else bag.append(0)
    

    


        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1
        training.append([bag,output_row])

    print(training)

    random.shuffle(training)
    training = np.array(training)


    x_train = list(training[:,0])
    y_train = list(training[:,1])
    print(x_train)
    print(y_train)
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



lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pickle','rb'))
classes = pickle.load(open('classes.pickle','rb'))
model = load_model('chatbot_model.h5')

def clean_up(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words=[lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i]=1
    return np.array(bag)

def predict(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1],reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent':classes[r[0]],'probability':str(r[1])})
    return return_list

def get_response(intent_list,intents_json):
    tag = intent_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag']==tag:
            result = random.choice(i['responses'])
            break
    return result