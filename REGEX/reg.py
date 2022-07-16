import re
import nltk
from nltk.stem import WordNetLemmatizer
stemmer = WordNetLemmatizer()

string = '''
    Fuck
    Fucking
    Fucker
    Fucked
    '''

find = nltk.word_tokenize(string)
for i in find:
    print(i)
    print(stemmer.lemmatize(i))



 