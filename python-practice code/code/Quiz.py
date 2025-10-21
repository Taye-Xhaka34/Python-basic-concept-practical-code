# Simple Quiz App in Python

# List of quiz questions and answers
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Paris", "b) Rome", "c) Madrid", "d) Berlin"],
        "answer": "a"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["a) Python", "b) HTML", "c) C++", "d) Java"],
        "answer": "b"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["a) 6", "b) 7", "c) 8", "d) 9"],
        "answer": "c"
    }
]

score = 0  # keep track of correct answers

print("Welcome to the Quiz App!\n")

# Loop through each question
for q in quiz:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    # Get user's answer
    answer = input("Enter your answer (a/b/c/d): ").lower()

    # Check if correct
    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong! The correct answer was:", q["answer"], "\n")

# Final score
print("Quiz completed!")
print("Your final score is:", score, "out of", len(quiz))
