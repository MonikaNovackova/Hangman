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

    def choose_two_characters(self):
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
        self.indecies = self.indecies | set(matching_indecies)

    def is_complete(self):
        return len(self.my_word) == len(self.indecies)

class Game:

    def __init__(self,list_of_words):
        word_string = list_of_words[random.randint(1,len(list_of_words))]
        self.word = Word(word_string)

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
        while not self.word.is_complete():
            print(self.word.show_current_guess())
            guessed_letter = self.get_guess()
            self.word.guess_a_letter(guessed_letter)

if __name__ == "__main__":
    x=Word('Christmas')
    print(x.my_word)
    print(x.indecies)
    print(x.show_current_guess())
    print(x.indecies)
    x.guess_a_letter('a')
    print(x.show_current_guess())
    print(x.is_complete())
    print('--------------------------------------------------------------------------------------------------------------------------------')
    y=Game(general_words)
    print(y.word.my_word)
    y.run_game()
