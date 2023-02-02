import random


def game_rule():
    print('What number is missing in the progression?')


def question_and_correct_answer():
    list_of_progression = []
    number = random.randint(0, 50)
    step_of_progression = random.randint(2, 8)
    length_of_progression = random.randint(5, 10)


    for _ in range(length_of_progression):
        number += step_of_progression
        list_of_progression.append(number)

    random_index = random.randint(0, length_of_progression - 1)
    missing_number = str(list_of_progression[random_index])
    list_of_progression[random_index] = '..'
    list_of_progression = " ".join(map(str, list_of_progression))
    return list_of_progression, missing_number
