#!/usr/bin/env python3
import random
import prompt


def is_simple(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


def start(username):
    name = username
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_answer = 0

    for _ in range(3):
        rand_num = random.randint(1, 100)
        print(f'Question: {rand_num}')
        simple = is_simple(rand_num)
        answer = prompt.string('Your answer: ')

        if answer == 'yes' or not simple:
            opposite_answer = 'no'
        else:
            opposite_answer = 'yes'

        if answer.lower() == 'yes' and simple:
            print('Correct!')
            count_answer += 1
        elif answer.lower() == 'no' and not simple:
            print('Correct!')
            count_answer += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was "
                  f"'{opposite_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if count_answer == 3:
        print(f'Congratulations, {name}!')
