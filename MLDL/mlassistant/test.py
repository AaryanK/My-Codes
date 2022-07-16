import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def clean_up(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words=[lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words



print(clean_up("HEy fucking hell, how are you? !!!"))