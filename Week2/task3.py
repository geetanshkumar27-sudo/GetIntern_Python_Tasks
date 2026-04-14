import random

secret = random.randint(1, 10)
guess = 0

print("Guess my number (1-10)!")

while guess != secret:
    guess = int(input("Your guess: "))
    if guess == secret:
        print("Correct! Won!")
    else:
        print("Wrong. Try again!")

print("Game Over!")
