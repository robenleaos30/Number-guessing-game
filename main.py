from art import logo
import random
print(logo)
number = random.randint(1, 100)
choice = input("Guess the number in 1 to 100 in this game.You can pick easy or hard.Lets pick!\n")


def easy():
    num = True
    lives = 0
    while num:
        guess = int(input('Guess the right number in 1 to 100.Good luck!\n'))
        if guess == number:
            print("You win! You pick the right number.")
            num = False
        if guess != number:
            lives += 1
            print(f"Now you have only {10 - lives} lives.Please focus!")
            if number > guess:
                print("Too low!")
            elif number < guess:
                print("Too high!")
            if lives == 10:
                print("Bad luck! Please try again.")
                num = False


def hard():
    num = True
    lives = 0
    while num:
        guess = int(input('Guess the right number in 1 to 100.Good luck!\n'))
        if guess == number:
            print("You win! You pick the right number.")
            num = False
        if guess != number:
            lives += 1
            if number > guess:
                print("Too low!")
            elif number < guess:
                print("Too high!")
            print(f"Now you have only {5 - lives} lives.Please focus!")
            if lives == 5:
                print("Bad luck! Please try again.")
                num = False


if choice == 'easy':
    easy()
elif choice == 'hard':
    hard()
else:
    print("You choose the level of number guessing game!")
    choice = input("Guess the number in 1 to 100 in this game.You can pick easy or hard.Lets pick!\n")