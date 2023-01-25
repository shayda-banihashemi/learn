import random

# Adding the words to the array
words = ["sunny", "windy", "rainy", "cloudy", "snowing", "blizzard", "flooding", "foggy", "humid", "breezy"]

# generating a random number that will pick individual word from the array of words
random = random.randrange(0, 11)

# Choosing the word for the puzzle
current_word = words[random]
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
hangman_array = []
hangman_array = ["*" for i in range(length)]
# print(hangman_array)

# This loop runs while the puzzle remains unsolved
while "*" in hangman_array:
    print(hangman_array)
    guess = input("Guess a letter ")

    # This loop searches the word for the letter guessed

    for x in range(0, length):
        if guess == word_array[x]:
            # print("This works")
            hangman_array[x] = guess
        # else:
        # print("That letter is not in the word")

print(hangman_array)
print("You Won! The word is " + current_word)
