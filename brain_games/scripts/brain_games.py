#!/usr/bin/env python3
from brain_games.scripts.cli import welcome_user


def greet(where):
    print(f'Welcome to the {where}!')


def main():
    greet('Brain Games')
    welcome_user()


if __name__ == '__main__':
    main()
