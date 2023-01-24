#!/usr/bin/env python3
def welcome_user():
    import prompt
    name = prompt.string('May I have your name? ')
def main():
    welcome_user()
if __name__ == '__main__':
    main()
