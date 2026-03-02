answered = 0
score = 0
print("Hello, welcome to the quiz!")

while True:
    print("1. What is the capital of Australia?")
    answer = input("Your answer: ")
    answered += 1
    if answer.lower() == "canberra":
        print("Correct!")
        score += 1
    else:        
        print("Incorrect. The correct answer is Canberra.")

    print("2. What is the largest planet in our solar system?")
    answer = input("Your answer: ") 
    answered += 1
    if answer.lower() == "jupiter":
        print("Correct!")
       
        score += 1
    else:        
        print("Incorrect. The correct answer is Jupiter.")

    print("3. Who wrote Romeo and Juliet?")
    answer = input("Your answer: ")
    answered += 1
    if answer.lower() == "william shakespeare":
        print("Correct!")
        score += 1
    else:        
        print("Incorrect. The correct answer is William Shakespeare.")

    #Print out score and percentage
    print(f"You have answered {answered} questions with a score of {score}.")
    print(f"You scored {score/answered*100:.2f}%.")
    break