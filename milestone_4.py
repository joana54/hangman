import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def __check_guess(self, guess):
        """This function takes in a guess argument and checks if it's in the self.word. Else it reduces number of lives
        and prints how many lives are left.""" 
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives -1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def __ask_for_input(self):
        """This function asks for an input from the user and checks whether the input is one alphabetical letter. Also checks
        has already been made. Returns the guess if valid."""
        while True:
            guess = input("Please enter one letter:")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                return guess

    def game(self):
        """This function runs while there are more than 0 lices left. It calls the check_guess() function and appends the guess
        to self.list_of_guesses."""
        while self.num_lives > 0:
            guess = Hangman.__ask_for_input(self)
            Hangman.__check_guess(self, guess)
            self.list_of_guesses.append(guess)

    

if __name__ == "__main__":

    hangman = Hangman(["mango", "pineapple", "kiwi", "strawberries", "quince"])

    hangman.game()

   

