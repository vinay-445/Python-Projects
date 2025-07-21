import random
import time
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def game_rules():
    print("\n")
    print("======================= Game Logic =======================")
    print("\n  Rock beats Scissors\n  Scissor beats paper\n  Paper beats rock")
    print("\nScore Rules")
    print("\n 1.No point for Tie\n 2.No point for Lose\n 3.Point for Win")
game_rules()
game=[Rock,Paper,Scissors]
user_score=0
computer_score=0
while True:
    print("\n0 for rock\n1 for paper\n2 for scissor\n")
    user_choice=input("Enter your choice: ")
    computer_choice=random.randint(0,2)
    if (user_choice=="exit"):
        break
    user_choice=int(user_choice)
    if(user_choice>=0 and user_choice<=2):
        print(game[user_choice])
        print(f"\ncomputer choice is {computer_choice}")
        print(game[computer_choice])
        if((user_choice>=0 and user_choice<=2)):
            if(user_choice==computer_choice):
                print("\nIt's a tie")
            elif(user_choice==0 and computer_choice==2):
                user_score+=1
                print("\nYou Win")
            elif(user_choice==2 and computer_choice==0):
                computer_score+=1
                print("\nYou Lose")
            elif(user_choice < computer_choice):
                computer_score+=1
                print("\nYou Lose")
            elif(user_choice > computer_choice):
                user_score+=1
                print("\nYou Win")
    else:
        print("Enter correct choice")
        break
    continue_playing=input("To play another round enter 'yes' or 'y' else 'no' or 'n' to quit:  ").lower()
    if continue_playing=='no' or continue_playing=='n':
        break
    else:
        print("Only enter 'yes/y' or 'no/n'")
print("Calculating Score please wait....")
time.sleep(1)
print(f"\nYour score is {user_score}  :  Computer score is {computer_score}")
print("\nThanks for playing the game....")