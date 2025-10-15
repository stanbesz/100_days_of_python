from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_q = Question(question["text"],question["answer"])
    question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)
next_question = quiz_brain.getTopQuestion()

while quiz_brain.quizHasQuestions():
    user_input = input(f"Q.{quiz_brain.question_number}: {next_question.text} (True/False): ").lower()
    quiz_brain.check_answer(user_input,next_question.answer)
    next_question = quiz_brain.getTopQuestion()

print("You've completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
print(question_bank)