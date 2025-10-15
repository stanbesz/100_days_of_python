
class QuizBrain:
    def __init__(self,q_list: list):
        self.question_number = 0
        self.score = 0
        self.question_list:list = q_list

    def quizHasQuestions(self):
        return self.question_number < len(self.question_list)
        
    def getTopQuestion(self):
        last_index = self.question_number
        self.question_number = self.question_number + 1
        return self.question_list[last_index]
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower():
            self.score+=1
            print(f"You got it right! Current score: {self.score}")
        else:
            print(f"That's wrong. Current score: {self.score}")
        print(f"The correct answer was: {correct_answer}.")