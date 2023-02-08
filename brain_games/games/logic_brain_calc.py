import random
GAME_RULE = 'What is the result of the expression?'
MIN = 5
MAX = 50


def question_and_correct_answer():

    first_operand = random.choice(range(MIN, MAX))
    operator = random.choice(['+', '-', '*'])
    second_operand = random.choice(range(MIN, MAX))

    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = str(eval(question))

    return question, correct_answer
