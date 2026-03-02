class Quiz:

    def __init__(self):
        self.questionbank =[]
        self.answerbank = []

    def addQuestion(self):
        numinput = int(input("How many questions would you like to add to the Quiz? "))
        for i in range(numinput):
            q = input("What question would you like to ask? ")
            a = input("What is the answer to that question? ")
            self.questionbank.append(q)
            self.answerbank.append(a.lower())
    
        self.runQuiz()

    def runQuiz(self):
        answered = 0
        score = 0

        print("Time to take the Quiz!")

        for i in range(len(self.questionbank)):
            answer = input(f"{self.questionbank[i]} ")        
            answered += 1
            if (answer.lower().strip() == self.answerbank[i]):
                score += 1
                print("Correct!")
            else: print(f"Incorrect! The answer is: {self.answerbank[i]}")
        
        print(f"You got {score} questions correct!")
        print(f"That's {(score/answered)*100:.2f}%")
        print ("Thank you for using the Quiz machine!")

def main():
    userinput = input("Would you like to add a questinon? (y/n):  ")
    if (userinput.lower() == 'y'):
        q1 = Quiz()
        q1.addQuestion()
    else: print ("Thank you for using the Quiz machine!")

if __name__ == "__main__":
    main()