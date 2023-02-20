import random
GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN = 5
MAX = 500


def is_prime(question):

    for i in range(2, question):
        if (question % i) == 0:
            return False

    return True


def question_and_correct_answer():
    question = random.randint(MIN, MAX)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
