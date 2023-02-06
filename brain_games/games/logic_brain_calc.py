import random


def game_rule():
    print('What is the result of the expression?')


def question_and_correct_answer():

    first_operand = random.choice(range(5, 60))
    operator = random.choice(['+', '-', '*'])
    second_operand = random.choice(range(5, 30))

    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = str(eval(question))

    return question, correct_answer
