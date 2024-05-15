#!/usr/bin/env python3
import random
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_answer = 0
    beg = 1
    end = 100

    for i in range(3):
        random_int = random.randint(beg, end)
        print(f'Question: {random_int}')
        answer = prompt.string('Your answer: ')

        if answer == 'yes':
            opposite_answer = 'no'
        else:
            opposite_answer = 'yes'

        if random_int % 2 == 0 and answer == 'yes':
            print('Correct!')
            count_answer += 1
        elif random_int % 2 != 0 and answer == 'no':
            print('Correct!')
            count_answer += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{opposite_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if count_answer == 3:
        print(f'Congratulations, {name}!')