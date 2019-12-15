import random
from listOfWords import ChristmasWords as words2

def CheckLetter(aword,aletter):
    return [counter for counter, value in enumerate(aword) if (value.upper()==aletter.upper())]

def ReplaceLetter(word1,word2,indecies):
    listW1=list(word1)
    listW2=list(word2)
    for i in indecies:
        listW1[i]=listW2[i]
    return("".join(listW1))
#------------------------------------------------------------------------------------------------------------------------------------------------------

def PickWord():
    i1=random.randint(1,len(words2))
    thepickedword=words2[i1]
    return(thepickedword)

theword=PickWord()

length=len(theword)
wordguessed=length* '*'
i2=[]
i2.append(random.randint(0,length-2))
i2.append(random.randint(i2[0]+1,length-1))




attempts=length*3

listch=[]

for counter,value in enumerate(wordguessed):
    if counter == (i2[0]):
        listch.append(theword[i2[0]])
    elif counter == (i2[1]):
        listch.append(theword[i2[1]])
    else:
        listch.append(value)

wordguessed="".join(listch)


print("You have %d attempts" % attempts)
print(wordguessed)

while (attempts>0) and (not wordguessed==theword):
    guess=str(0)
    while (not (guess.isalpha()  and len(guess)==1)):
        guess=input("For exit press Q. Otherwise please insert a letter:     ")
        if (not guess.isalpha()):
            print("This is not a letter. Try again.")
        if (len(guess)>1):
            print("This is too long.give me a ONE single letter:    ")
        if guess =='Q':
            exit('Bbyyyee')
    if theword.count(guess)>0:
        hitIndecies=CheckLetter(theword,guess)
        wordguessed=ReplaceLetter(wordguessed,theword,hitIndecies)
        print(wordguessed)
    attempts=attempts-1
    print("You have %d attempts" % attempts)

if attempts==0:
    exit("Noo.You lost....")

exit("HURRAY, YOU WON")



theword.count(guess)
