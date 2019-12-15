import random
from listOfWords import *

def CheckLetter(aword,aletter):
    return [counter for counter, value in enumerate(aword) if (value==aletter)]

def ReplaceLetter(word1,word2,indecies):
    listW1=list(word1)
    listW2=list(word2)
    for i in indecies:
        listW1[i]=listW2[i]
    return("".join(listW1))
#------------------------------------------------------------------------------------------------------------------------------------------------------

# choose a word randomly from a list of words
def PickWord():
    i1=random.randint(1,len(words2))
    return(words2[i1])

theword=PickWord()


def HiddeWordToGuess(someword):
    """
    Takes a word, returns a string of stars (*) with two random letters of the original word showing
    """
    length=len(someword)
    starword=length* '*'
    visible_letters_index=[]
    visible_letters_index.append(random.randint(0,length-2))
    visible_letters_index.append(random.randint(visible_letters_index[0]+1,length-1))
    mix_letter_stars=[]
    for counter,value in enumerate(starword):
        if counter == (visible_letters_index[0]):
            mix_letter_stars.append(someword[visible_letters_index[0]])
        elif counter == (visible_letters_index[1]):
            mix_letter_stars.append(someword[visible_letters_index[1]])
        else:
            mix_letter_stars.append(value)

    return "".join(mix_letter_stars)



wordguessed=HiddenWordToGuess(theword)


attempts=length(wordguessed)*3
print("You have %d attempts" % attempts)
print(wordguessed)


def get_valid_guess():
    """
    keep asking the user for input until they enter a valid
    """
    guess=str(0)
    while (not (guess.isalpha()  and len(guess)==1)):
        guess=input("For exit press Q. Otherwise please insert a letter:     ")
        if (not guess.isalpha()):
            print("This is not a letter. Try again.")
        if (len(guess)>1):
            print("This is too long.give me a ONE single letter:    ")
        if guess =='Q':
            exit('Bbyyyee')
    return guess


while (attempts>0) and (not wordguessed==theword):

def GameRound(current_attempts,aword):
    guess = get_valid_guess()
    if theword.count(guess)>0:
        hitIndecies=CheckLetter(theword,guess)
        wordguessed=ReplaceLetter(wordguessed,theword,hitIndecies)
        print(wordguessed)

    attempts=attempts-1
    print("You have %d attempts" % attempts)

if attempts==0:
    exit("Noo.You lost....")


def show_intro_text():
    """
    Show introduction text and instructions to user
    """
    print("Welcome to hangman game...")

def create_word_to_show(answer, guesses):
    """
    Takes the full correct word, and the valid guesses and generates a asterisk populated string1
    """
    return "****a**c"

def start_game_loop():
    word_to_guess = PickWord()
    correct_guessed_indexes = [] // Fill with indexes of valid correct_guessed_indexes
    // Populate with initial correct_guessed
    correct_guessed_indexes = [ 2, 3]
    word_to_show = create_word_to_show(word_to_guess, correct_guessed_indexes)

def main_loop():
    show_intro_text()
    start_game_loop()

exit("HURRAY, YOU WON")

if __name__ == "__main__":
    main_loop()



theword.count(guess)
