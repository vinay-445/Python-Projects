import random
import Guess_the_number_logo
print(Guess_the_number_logo.logo)
print("let me think of a number 1 to 50.")
number=random.randint(1,50)
level=input("Choose the level of difficulty...Type 'easy' or 'moderate' or 'hard': ")
def condition(attempts,total_attempts):
    while (attempts!=0):
        guess=int(input("Make a guess: "))
        if guess>number:
            attempts=attempts-1
            print("Your guess is too high")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number!")
        elif (guess<number):
            attempts=attempts-1
            print("Your guess is too low")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number!")
        elif (guess==number):
            print(f"Your guess is correct and the number is {number}")
            print(f"You have finished within {total_attempts-attempts} attempts")
            exit()
        else:
            attempts=attempts-1
            print("Guessed number should be in range.")
    print("You are out of guesses...You lose!!")
def level_easy():
    attempts=15
    total_attempts=15
    print("You have 15 attemps remaining to guess the number!")
    condition(attempts,total_attempts)
def level_moderate():
    attempts=10
    total_attempts=10
    print("You have 10 attemps remaining to guess the number!")
    condition(attempts,total_attempts)
def level_hard():
    attempts=5
    total_attempts=5
    print("You have 5 attemps remaining to guess the number!")
    condition(attempts,total_attempts)
if level=='easy':
    level_easy()
elif level=='moderate':
    level_moderate()
elif level=='hard':
    level_hard()
else:
    print("Enter correct choice")