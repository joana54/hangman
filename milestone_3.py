import random

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")



def ask_for_input():
    while True:
        guess = input("Please enter one letter:")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)



if __name__ == "__main__":
    word_list = ["mango", "pineapple", "kiwi", "strawberries", "quince"]
    print(word_list)

    word = random.choice(word_list)
    print(word)
    ask_for_input()