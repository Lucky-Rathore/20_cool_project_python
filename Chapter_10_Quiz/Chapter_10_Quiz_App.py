# Chapter_10_Quiz_App
import json

def load_quiz_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def run_quiz(quiz_data):
    score = 0
    for question in quiz_data:
        print(question['question'])
        for index, option in enumerate(question['options']):
            print(f"{index + 1}: {option}")
        answer = int(input("Enter the number of your answer: ")) - 1
        
        if question['options'][answer] == question['answer']:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {question['answer']}\n")

    print(f"You've completed the quiz! Your final score is {score}/{len(quiz_data)}")

def main():
    file_path = 'quiz_data.json'  # This should be your JSON file containing quiz questions.
    quiz_data = load_quiz_data(file_path)
    run_quiz(quiz_data)

if __name__ == "__main__":
    main()