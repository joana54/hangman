import random
word_list = ["mango", "pineapple", "kiwi", "strawberries", "quince"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter one letter:")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.")
