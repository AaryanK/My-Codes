from tensorflow.keras.models import load_model
import nltk
import json
import numpy as np


intents = json.load(open('intents.json'))
model = load_model('chatbot_model.h5')
category = []
words = []
for i in intents['intents']:

    category.append(i['tag']) if i['tag'] not in category else None
    for j in i['patterns']:
        words.extend(nltk.tokenize.word_tokenize(j))

 
words = sorted(set(words))

def clean_up(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i]=1
    return np.array(bag)

bow = bag_of_words("what is your name")
predicted = model.predict(np.array([bow]))[0]
print(predicted)
ERROR_THRESHOLD = 0.25
results = [[i,r] for i,r in enumerate(predicted) if r > ERROR_THRESHOLD]
print(results)
# results.sort(key=lambda x: x[1],reverse=True)
# print(results)
return_list = []
for r in results:
    return_list.append({'category':category[r[0]],'probability':str(round(r[1]*100))+"%"})
return_list.sort(key=lambda x: x['probability'])
print(return_list[-1])


