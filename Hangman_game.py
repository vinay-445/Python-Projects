import random
import hangman_stages
import word_file
lives=6
choosen_word=random.choice(word_file.words)
choosen_word=choosen_word.lower()
length=len(choosen_word)
print("Welcome to Hangman game")
display=[]
for i in range(length):
    display += '_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(length):#apple
        letter=choosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    if guessed_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("\n")
            print("You Lose")
            print(f"The word is {choosen_word}")
    if '_' not in display:
        game_over=True
        print("\n")
        print("You win")
    print(hangman_stages.stages[lives])
    print(' '.join(display))