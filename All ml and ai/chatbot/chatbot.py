import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pickle','rb'))
classes = pickle.load(open('classes.pickle','rb'))
model = load_model('model.h5')

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
    list_of_intents = intents_json['main_intents']
    for i in list_of_intents:
        if i['cat']==tag:
            result = i['cat']
            break
    return result

print('Come on lets talk Aaryan')

# while True:
#     message = input('')
#     ints = predict(message)
#     res = get_response(ints,intents)
#     print(res)
#     if res in ["Bye","See you soon","Okay,bye have a nice one"]:
#         break
    

print(clean_up("Hey fucking little fool fuck you"))
bag = [0]*len(words)
for w in clean_up("Hey fucking little fool fuck you"):
    for i,word in enumerate(words):
        if word == w:
            bag[i]=1
print(np.array(bag))
bag = np.array(bag)
arr = model.predict(np.array([bag]))[0]
ERROR_THRESHOLD = 0.25
results = [[i,r] for i,r in enumerate(arr) if r > ERROR_THRESHOLD]
results.sort(key=lambda x: x[1],reverse=True)
return_list = []
for r in results:
    return_list.append({'intent':classes[r[0]],'probability':str(r[1])})
print(return_list)