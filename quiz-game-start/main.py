from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []
for questions in question_data:
    questions_text = questions["text"]
    questions_answer = questions["answer"]
    new_question = Questions(questions_text, questions_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_questions()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(questions_bank)}")


