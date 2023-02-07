import random
import math


def game_rule():
    print('Find the greatest common divisor of given numbers.')


def question_and_correct_answer():
    first_number = random.choice(range(50))
    second_number = random.choice(range(50))
    question = f'{first_number} {second_number}'
    correct_answer = str(math.gcd(first_number, second_number))

    return question, correct_answer
