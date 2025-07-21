import random
import os
import Higher_lower_game_logo
import Higher_lower_game_data
print(Higher_lower_game_logo.logo)
def account_info(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name},a {description} from {country}"
def followers(guess,follower1,follower):
    if follower1<follower2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False

score=0
continue_flag=True
account2=random.choice(Higher_lower_game_data.data)
while continue_flag:
    account1=account2
    account2=random.choice(Higher_lower_game_data.data)
    while account1==account2:
        account2=random.choice(Higher_lower_game_data.data)
    print(f"Compare 1: {account_info(account1)}")
    print(Higher_lower_game_logo.vs)
    print(f"Compare 2: {account_info(account2)}")
    follower1=account1["follower_count"]
    follower2=account2["follower_count"]
    guess=int(input("Who has more followers. Type 1 or 2: "))
    is_correct=followers(guess,follower1,follower2)
    print(follower1)
    print(follower2)
    os.system('cls')
    print(Higher_lower_game_logo.logo)
    if is_correct==True:
        score=score+1
        print(f"Your guess is correct and your score is {score}")
    else:
        continue_flag=False
        print(f"Your are wrong and your final score is {score}")