import quiz_questions
import random
import time

print(quiz_questions.logo)
print("Welcome to Quiz Game")
print("************************")
print("Choose an option from the below questions\nfor correct you get 1 point\nfor wrong you get 0 point")

points = 0
asked_questions = []
attempted = 0

def level(no_of_questions):
    if no_of_questions == 'easy':
        return 5
    elif no_of_questions == 'moderate':
        return 10
    elif no_of_questions == 'hard':
        return 15
    else:
        print("Invalid option")
        return 0

def check_answer(user_input, correct_answer):
    global attempted, points
    if user_input not in ['a', 'b', 'c', 'd']:
        print("Enter from the above options")
    else:
        attempted += 1
        if user_input == correct_answer:
            points += 1
            print("Correct answer")
        else:
            print("Incorrect answer")
        print(f"Your current score is {points}")

no_of_questions = input("Choose the level\neasy\nmoderate\nhard: \n").lower()
length = level(no_of_questions)

if length == 0:
    print("Invalid option")
else:
    for _ in range(length):
        if len(asked_questions) == len(quiz_questions.quiz["questions"]):
            print("All questions are completed.")
            break
        
        random_question = random.choice(quiz_questions.quiz["questions"])
        while random_question in asked_questions:
            random_question = random.choice(quiz_questions.quiz["questions"])
        
        asked_questions.append(random_question)
        print("\n")
        print(random_question["question"])
        for option, answer in random_question["options"].items():
            print(f"{option.upper()}: {answer}")
        
        user_input = input("Choose (A/B/C/D) or type 'exit' to quit: ").lower()
        if user_input == "exit":
            print("You have quitted the quiz")
            break
        check_answer(user_input, random_question["answer"])

    if user_input != "exit":
        print("You have successfully completed the quiz")
        print("Wait for a while, calculating results...")
        time.sleep(2)
        print(f"Your final score is {points}/{attempted}")
        if attempted > 0:
            print(f"Your final score percentage is {round((points / attempted) * 100, 2)}%")
        else:
            print("No questions attempted.")