import random
GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN = 5
MAX = 500


def is_prime(num):
    number_div = 0
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


def question_and_correct_answer():
    question = random.randint(MIN, MAX)
    i = 5
    while question % i != 0:
        i += 1
    correct_answer = i == question and "yes" or "no"
    return question, correct_answer
