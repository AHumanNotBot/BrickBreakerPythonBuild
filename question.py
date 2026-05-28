import random
class Question:
    def __init__(self, questionText = "", choice1 = "", choice2 = "", choice3 = "", choice4 = ""):
        self.questionText = questionText
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
        self.questions = open("questions.txt", "r").readlines()
        self.correctAnswer = 0
    def chooseQuestion(self):
        question = random.choice(self.questions)
        self.question = question.split("|")[0]
        self.choice1 = question.split("|")[1]
        self.choice2 = question.split("|")[2]
        self.choice3 = question.split("|")[3]
        self.choice4 = question.split("|")[4]
        self.correctAnswer = int(question.split("|")[5])


