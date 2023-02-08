import random
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN = 0
MAX = 100


def question_and_correct_answer():
    question = random.randint(MIN, MAX)
    correct_answer = question % 2 == 0 and 'yes' or 'no'
    return question, correct_answer
