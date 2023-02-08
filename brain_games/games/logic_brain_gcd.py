import random
import math
GAME_RULE = 'Find the greatest common divisor of given numbers.'
MIN = 1
MAX = 50


def question_and_correct_answer():
    first_number = random.choice(range(MIN, MAX))
    second_number = random.choice(range(MIN, MAX))
    question = f'{first_number} {second_number}'
    correct_answer = str(math.gcd(first_number, second_number))

    return question, correct_answer
