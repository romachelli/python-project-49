import prompt


def greeting_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    return print(f'Hello, {name}!')


def logic_brain_games(game):
    greeting_user()
    game.game_rule()
    winner = f'Congratulations, {name}!'
    correct_result = 'Correct!'
    game_rounds = 3

    for _ in range(game_rounds):
        question, correct_answer = game.question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        losing_the_game = (f'''{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!''')


        if user_answer != correct_answer:
            return print(losing_the_game)
        else:
            print(correct_result)


    return print(winner)
