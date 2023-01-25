import random

while True:
    secret_number = random.randrange(1, 101)
    print("This is the secret_number I am thinking of: ")
    print(secret_number)
    score = 100

    while True:

        guess = int(input("What secret_number am I thinking of? "))

        if guess == secret_number:
            print(f"You won! Your score is: {score}")
            break
        score -= 10
        print(f"Your score is {score}")
        if guess > secret_number:
            print("You guessed too high")
        else:
            print("You guessed to low")

    yorn = input("Play again? y/n ")

    if yorn != "y":
        break

print("Goodbye")