import random


def game_rule():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def question_and_correct_answer():
    question = random.randint(5, 500)
    i = 5
    while question % i != 0:
        i += 1
    correct_answer = i == question and "yes" or "no"
    return question, correct_answer
