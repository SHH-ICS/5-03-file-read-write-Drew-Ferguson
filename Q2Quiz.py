# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
# Program to read questions from a file and quiz the user

score = 0

try:
    with open("questions.txt", "r") as file:
        questions = file.read().strip().split("\n\n") 

    for question_block in questions:
        lines = question_block.split("\n")
        question = lines[0].replace("Question: ", "") 
        answers = lines[1:5]  
        correct_answer = lines[5].replace("Correct Answer: ", "").strip()

        print(f"\n{question}")
        for answer in answers:
            print(answer)

        user_answer = input("Your answer (A, B, C, or D): ").upper()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

    print(f"\nQuiz complete! You scored {score} out of {len(questions)}.")

except FileNotFoundError:
    print("Error: The file 'questions.txt' was not found. Please create questions first.")
except Exception as e:
    print(f"An error occurred: {e}")
