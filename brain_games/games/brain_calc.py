#!/usr/bin/env python3
import random
import prompt


def start(username):
    name = username
    print('What is the result of the expression?')
    count_answer = 0
    sign = ['+', '-', '*']
    beg = 1
    end = 100

    for _ in range(3):
        random_int_one = random.randint(beg, end)
        random_int_two = random.randint(beg, end)
        random_sign = random.choice(sign)
        print(f'Question: {random_int_one} {random_sign} {random_int_two}')
        answer = prompt.string('Your answer: ')

        if random_sign == '+':
            result = random_int_one + random_int_two
        elif random_sign == '-':
            result = random_int_one - random_int_two
        else:
            result = random_int_one * random_int_two

        if answer == str(result):
            print('Correct!')
            count_answer += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
    if count_answer == 3:
        print(f'Congratulations, {name}!')
