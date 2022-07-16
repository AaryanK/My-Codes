a = open('pasess.txt','r+')

lines = a.readlines()


SITES=[]
PASSWORDS=[]

def getpasswordsandusername():
    for i in range (len(lines)):
        if i % 2 ==1:
            PASSWORDS.append(lines[i].strip())
        if i % 2 ==0:
            SITES.append(lines[i].strip())
    return SITES,PASSWORDS







