
print("==============================")
print("       PYTHON QUIZ MASTER")
print("==============================")

name = input("Enter your name: ")

print(f"\nWelcome, {name}!")
print("Get ready to test your knowledge!")


questions = [
    {
        "question": "What does HTML stand for?",
        "options": {
            "A": "Hyper Text Markup Language",
            "B": "High Transfer Machine Language",
            "C": "Home Tool Markup Language",
            "D": "Hyperlinks Text Management Language"
        },
        "answer": "A"
    },
    {
        "question": "Which language is used for Python development?",
        "options": {
            "A": "HTML",
            "B": "CSS",
            "C": "Python",
            "D": "SQL"
        },
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "A": "//",
            "B": "#",
            "C": "/*",
            "D": "<!--"
        },
        "answer": "B"
    }
]

score = 0

for question in questions:
    print("\n------------------------------")
    print(question["question"])

    for option, answer in question["options"].items():
        print(f"{option}. {answer}")

    user_answer = input("Your answer (A, B, C or D): ")

    if user_answer.upper() == question["answer"]:
        print("Correct! Well done!")
        score += 1
    else:
        print("Wrong answer!")
        print(f"The correct answer is {question['answer']}")

print("\n==============================")
print("         QUIZ RESULTS")
print("==============================")
print(f"Your final score is: {score}/{len(questions)}")

