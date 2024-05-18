#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count_answer = 0
    beg = 1
    end = 100

    for _ in range(3):
        random_int_one = random.randint(beg, end)
        random_int_two = random.randint(beg, end)
        print(f'Question: {random_int_one} {random_int_two}')
        num = gcd_fun(random_int_one, random_int_two)
        print(num)
        answer = prompt.string('Your answer: ')


        if answer == str(num):
            print('Correct!')
            count_answer += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{num}'.")
            print(f"Let's try again, {name}!")
            break
    if count_answer == 3:
        print(f'Congratulations, {name}!')