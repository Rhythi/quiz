# function for greeting the user

def greet_user():
    name = input("Enter your name : ")
    print(f"\nWelcome,{name}! Let's begin your quiz!\n")
    print("Select options such as A,B.....")

# function for starting quiz

import random

def start_quiz():
    quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Lisbon"],
        "answer": "C. Paris"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Leo Tolstoy", "D. Mark Twain"],
        "answer": "B. William Shakespeare"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B. Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B. Blue Whale"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["A. Abraham Lincoln", "B. George Washington", "C. John Adams", "D. Thomas Jefferson"],
        "answer": "B. George Washington"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B. Carbon Dioxide"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1952"],
        "answer": "B. 1947"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Quartz"],
        "answer": "C. Diamond"
    },
    {
        "question": "Which continent is known as the 'Dark Continent'?",
        "options": ["A. Asia", "B. Africa", "C. South America", "D. Australia"],
        "answer": "B. Africa"
    },
    {
        "question": "Who invented the light bulb?",
        "options": ["A. Isaac Newton", "B. Nikola Tesla", "C. Albert Einstein", "D. Thomas Edison"],
        "answer": "D. Thomas Edison"
    }
    ]

    random.shuffle(quiz)

    answer =""
    correct_count=0
    wrong_count=0
    total_count=0
    wrong = {}
    for i in quiz:
       answer = input(f"\n{i["question"]}\n{i["options"]}\n").upper()[0]
       if answer == i["answer"][0]:
         print("correct answer! Keep going.....")
         correct_count+=1
         total_count+=1
       else:
         print("better luck next time !!!")
         wrong_count+=1
         total_count+=1
         wrong[i["question"]]=i["answer"]

    print("\nCorrect answers for the answers you have skipped and wronged")
    print("=============================================================\n")
    for i in wrong:
       print(f"\n{i}\n{wrong.get(i)}")

    print(f"\n{correct_count} out of {total_count}\n")
    print(f"{int((correct_count*100)/total_count)}%\n")
    if int((correct_count*100)/total_count) >95:
       print("Outstanding!")
    elif int((correct_count*100)/total_count) >=80 and int((correct_count*100)/total_count) <95:
       print("Great job!")
    elif int((correct_count*100)/total_count) >=50 and int((correct_count*100)/total_count) < 80:
       print("Good effort!")
    else:
       print("Keep practicing!")


# function for retry quiz

def retry_quiz():
   choice = ""
   choice = input("\nDo you want to restart the quiz again?(Y/N)").lower()
   if choice == "y":
      start_quiz()
   else:
      print("\nThank you for attending the quiz have a nice day !")
      print("*****************************************************\n")

      


