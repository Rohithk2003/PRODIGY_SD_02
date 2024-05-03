import random as r

attempts = 0
guess = 0
number = r.randint(1, 100)
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    attempts += 1
print("You got it in", attempts, "attempts")
