from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
quiz = QuizBrain(question_bank)
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_qn = Question(question_text,question_answer)
    question_bank.append(new_qn)


while quiz.still_has_questions():
    quiz.next_question()

print("Thank you for playing!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

