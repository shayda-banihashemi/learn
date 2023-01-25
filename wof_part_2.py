import random

# Adding the words to the array
words = ["sunny", "windy", "rainy", "cloudy", "snowing", "blizzard", "flooding", "foggy", "humid", "breezy"]

# generating a random number that will pick individual word from the array of words
# the behavior of random has been changed since it has been defined as a variable.
current_word = random.choice(words)

print(current_word)

# Getting the length of letters in the word
length = len(current_word)
# print(length)

# Putting the word in an array of individual characters
word_array = []
for letter in current_word:
    word_array.append(letter)
# print(word_array)

# Starting a new game and filling the puzzle with *'s
secret_word = len(current_word) * "_"
# print(hangman_array)

# This loop runs while the puzzle remains unsolved
while "_" in secret_word:
    print(secret_word)
    guess = input("Guess a letter ")

    if guess not in current_word:
        print("You guess incorrectly ")
        continue
    for position,letter in enumerate(current_word):
        if guess == letter:
            secret_word=list(secret_word)
            secret_word[position]=letter
            secret_word="".join(secret_word)
    if secret_word==current_word:
        print("You Won! The word is " + secret_word)
        break



