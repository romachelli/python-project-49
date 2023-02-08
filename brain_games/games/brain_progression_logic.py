import random
GAME_RULE = 'What number is missing in the progression?'
MIN = 0
MAX = 100
STEP_MIN = 2
STEP_MAX = 8
LEN_MIN = 5
LEN_MAX = 10


def question_and_correct_answer():
    list_of_progression = []
    number = random.randint(MIN, MAX)
    step_of_progression = random.randint(STEP_MIN, STEP_MAX)
    length_of_progression = random.randint(LEN_MIN, LEN_MAX)

    for _ in range(length_of_progression):
        number += step_of_progression
        list_of_progression.append(number)

    random_index = random.randint(0, length_of_progression - 1)
    missing_number = str(list_of_progression[random_index])
    list_of_progression[random_index] = '..'
    list_of_progression = " ".join(map(str, list_of_progression))
    return list_of_progression, missing_number
