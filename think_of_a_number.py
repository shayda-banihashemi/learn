import random

number = random.randrange(1, 101)
print("This is the number I am thinking of: ")
print(number)

guess = int(input("What number am I thinking of? "))

if guess == number:
    print("You got it on your first try!")
    exit()

while guess != number:
    if guess > number:
        guess = int(input("You are too high, guess again: "))
    elif guess < number:
        guess = int(input("You are too low, guess again: "))

if guess == number:
    print("You got it !")
