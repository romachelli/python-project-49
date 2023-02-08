import prompt
print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
game_rounds = 3


def greeting_user():
    return print(f'Hello, {name}!')


def logic_brain_games(game):
    greeting_user()
    print(game.GAME_RULE)

    for _ in range(game_rounds):
        question, correct_answer = game.question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            return print(f'"{user_answer}" is wrong answer ;(.'
                         f'Correct answer was "{correct_answer}".'
                         f"\nLet's try again, {name}!")

    return print(f'Congratulations, {name}!')
