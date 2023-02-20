import random
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN = 0
MAX = 100


def is_even(question):
    return question % 2 == 0


def question_and_correct_answer():
    question = random.randint(MIN, MAX)
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer
