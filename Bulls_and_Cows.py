import random
import string
def main():
    def game_rules():
        print("Game Rules:")
        print("1. Each digit or character is unique.")
        print("2. A bull means one digit (or letter) is correct and in the correct position.")
        print("3. A cow means one digit (or letter) is correct but in the wrong position.")

    def generate_unique_number():
        while True:
            num = str(random.randint(1000, 9999))
            if len(set(num)) == 4:
                return num

    def generate_unique_string(length):
        characters = string.ascii_lowercase
        return ''.join(random.sample(characters, length))

    game_rules()
    user_choice = input("Enter your choice (number or word): ").strip().lower()

    if user_choice == "number":
        secret = generate_unique_number()
        print("A 4-digit number has been generated.")
    elif user_choice == "word":
        secret = generate_unique_string(4)
        print("A 4-letter word has been generated.")
    else:
        print("Invalid choice")
        exit()

    tries_mode=input("Enter 'e' for easy level \n          or\n'm' for medium level \n          or\n'h' for hard level\n          or\nEnter mychoice for your number of tries\n")

    if tries_mode=="e":
        tries=15
    elif tries_mode=="m":
        tries=10
    elif tries_mode=="h":
        tries=5
    elif tries_mode=="mychoice":
        tries = int(input("Enter the number of tries you need: "))
    else:
        print("Enter from the above options")

    # print(secret)

    while tries > 0:
        user_input = input("Enter your guess: ").strip()

        if len(user_input) != 4:
            print("Please enter a 4-digit number or a 4-letter word.")
            tries -= 1
            print(f"You have {tries} tries left.\n")
            continue

        bulls = 0
        cows = 0

        for i in range(4):
            if user_input[i] == secret[i]:
                bulls += 1
            elif user_input[i] in secret:
                cows += 1

        print(f"{bulls} bulls, {cows} cows")

        if bulls == 4:
            print("Congratulations! You guessed correctly.")
            break

        tries -= 1
        print(f"You have {tries} tries left.\n")

    if tries == 0:
        print("Sorry, you've run out of tries. The secret was:", secret)
if __name__=="__main__":
    main()