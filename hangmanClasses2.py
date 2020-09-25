import random
from listOfWords import general_words

class Word:
    """
    A word to guess
    """
    def __init__(self,input):
        self.my_word = input
        self.indecies = set()
        self.choose_two_characters()

    def __len__(self):
        return len(self.my_word)

    def choose_two_characters(self):
        """
        chooses two indecies of letters of the word, which are depicted at the beginning
        """
        length=len(self.my_word)
        first_index=random.randint(0,length-2)
        self.indecies.add(first_index)
        self.indecies.add(random.randint(first_index+1,length-1))

    def show_current_guess(self):
        length=len(self.my_word)
        listW1 = list(length* '*')
        listW2 = list(self.my_word)
        for i in self.indecies:
            listW1[i]=listW2[i]
        return("".join(listW1))

    def guess_a_letter(self,aletter):
        matching_indecies = [counter for counter, value in enumerate(self.my_word) if (value.upper()==aletter.upper())]
        guessed_previously = aletter in [self.my_word[index] for index in self.indecies]
        """ I think that this returns true or false. true if the letter was guessed previously"""
        self.indecies = self.indecies | set(matching_indecies)
        is_the_guess_correct = len(matching_indecies) > 0
        return guessed_previously, is_the_guess_correct

    def is_complete(self):
        return len(self.my_word) == len(self.indecies)

class Game:

    def __init__(self,list_of_words):
        word_string = list_of_words[random.randint(1,len(list_of_words))]
        self.word = Word(word_string)
        self.attempts=3*(len(self.word)-1)
        self.play_again='Yes'

    @staticmethod
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


    def get_guess(self):
        currently_guessed_letter=str(0)
        while (not (currently_guessed_letter.isalpha()  and len(currently_guessed_letter)==1)):
            currently_guessed_letter=input("For exit press Q. Otherwise please insert a letter:     ")
            if (not currently_guessed_letter.isalpha()):
                print("This is not a letter. Try again.")
            if (len(currently_guessed_letter)>1):
                print("This is too long.give me a ONE single letter:    ")
            if currently_guessed_letter =='Q':
                exit('Bbyyyee')
        return currently_guessed_letter

    def run_game(self):
        self.show_intro_text()
        while not (self.word.is_complete() or self.attempts==0):
            print('You have '+str(self.attempts)+' attempts remaining')
            print(self.word.show_current_guess())
            guessed_letter = self.get_guess()
            guessed_before, guess_correct = self.word.guess_a_letter(guessed_letter)
            if (not guess_correct) or guessed_before:
                self.attempts = self.attempts -1
        if self.word.is_complete():
            print('Hurray, you win. The word is '+self.word.my_word.upper())
        elif self.attempts==0:
            print('Noo, you loose :-(..But its not the end of the word. And besides..you can try again..??:-)')



if __name__ == "__main__":
    print('--------------------------------------------------------------------------------------------------------------------------------')
    while True:
        y=Game(general_words)
        y.run_game()
