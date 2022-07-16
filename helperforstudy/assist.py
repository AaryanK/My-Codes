from sympy import N
from PyDictionary import PyDictionary

dictionary=PyDictionary()
def give_synonym(word):
    synonym = dictionary.synonym(word)
    return synonym

def give_antonym(word):
    antonym = dictionary.antonym(word)
    return antonym

def give_meaning(word):
    meaning = dictionary.meaning(word)
    if meaning=="Error: A Term must be only a single word" or not meaning:
        return f"No meaning found for {word}" 
    else:
        text = f'{word} can be used as '
        if len(meaning)>1:
            for j in meaning:
                if list(meaning)[-1]!=j:
                    text+=f"{j},"
                else:
                    text+=f"{j}\n"
        else:
            for j in meaning:
                text+=f"a {j}\n"
        count = 1
        for i in meaning:
            text += f"\n{count} {i}\n"
            for z in meaning[i]:
                text += f"  •{z}\n"
            count +=1
            text+="\n"
        text+=f"Synonyms of {word} are:\n"
        for i in give_synonym(word):
            text += f"  •{i}\n"
        text+="\n"
        text+=f"Antonyms of {word} are:\n"
        for i in give_antonym(word):
            text += f"  •{i}\n"
        return text



