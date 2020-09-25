import random
from listOfWords import general_words

def finding_indecies_to_replace(aword,aletter):
    return [counter for counter, value in enumerate(aword) if (value.upper()==aletter.upper())]

def ReplaceLetter(word1,word2,indecies):
    listW1=list(word1)
    listW2=list(word2)
    for i in indecies:
        listW1[i]=listW2[i]
    return("".join(listW1))

def PickWord(list_of_words):
    """
    Picks a word from a list of words and also selects indecies of letters to be shown
    """
    i1=random.randint(1,len(list_of_words))
    length=len(list_of_words[i1])
    indecies_letters_to_show=[]
    indecies_letters_to_show.append(random.randint(0,length-2))
    indecies_letters_to_show.append(random.randint(indecies_letters_to_show[0]+1,length-1))

    return list_of_words[i1], indecies_letters_to_show
#------------------------------------------------------------------------------------------------------------------------------------------------------

def show_intro_text():
    """
    Show introduction text and instructions to user
    """
    user_response=str(0)
    print("Welcome to hangman game")
    while (  not(user_response.lower() == 'y') and not(user_response.lower() == 'q') ):
        user_response = input("Would you like to play? If yes, press 'y'. Or for exit press 'q'.")
        if user_response.lower()=='q':
            exit('Bye')

def create_word_to_show(answer, guesses):
    """
    Takes the full correct word, and the valid guesses and generates a asterisk populated string1
    """
    length=len(answer)
    wordguessed = list(length* '*')
    answer=list(answer)
    wordguessed[guesses[0]] = answer[guesses[0]]
    wordguessed[guesses[1]] = answer[guesses[1]]

    return ''.join(wordguessed)

def GameRound(no_attempts,word_to_show,word_to_guess,indecies_of_letters_to_show):
    print("Guess a Christmas or Codebar-related word. "+"You have %d no_attempts" % no_attempts)
    print(word_to_show)
    guess=str(0)
    while (not (guess.isalpha()  and len(guess)==1)):
        guess=input("For exit press Q. Otherwise please insert a letter:     ")
        if (not guess.isalpha()):
            print("This is not a letter. Try again.")
        if (len(guess)>1):
            print("This is too long.give me a ONE single letter:    ")
        if guess =='Q':
            exit('Bbyyyee')
    if guess in word_to_guess:
        hitIndecies = finding_indecies_to_replace(word_to_guess,guess)
        indecies_of_letters_to_show = indecies_of_letters_to_show+hitIndecies
        word_to_show = ReplaceLetter(word_to_show,word_to_guess,indecies_of_letters_to_show)

    return word_to_show, indecies_of_letters_to_show


def game_loop():
    word_to_guess, indecies_of_letters_to_show = PickWord(general_words)

    # Fill with indexes of valid correct_guessed_indexes
    # Populate with initial correct_guessed
    word_to_show = create_word_to_show(word_to_guess, indecies_of_letters_to_show)
    attempts=3*(len(word_to_guess)-1)
    while (attempts>0) and (not word_to_guess==word_to_show):
        word_to_show, indecies_of_letters_to_show = GameRound(attempts,word_to_show,word_to_guess,indecies_of_letters_to_show)
        attempts=attempts-1
        if attempts==0:
            exit("Noo.You lost....the word was " + word_to_guess.upper())
    print(word_to_show.upper())
    exit("HURRAY, YOU WON")

def main_loop():
    show_intro_text()
    game_loop()

if __name__ == "__main__":
    main_loop()
