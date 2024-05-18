#!/usr/bin/env python3
import random
import prompt

def is_simple(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_answer = 0

    for _ in range(3):
        rand_num = random.randint(1, 100)
        print(f'Question: {rand_num}')
        simple = is_simple(rand_num)
        print(simple)
        answer = prompt.string('Your answer: ')


        if answer.lower() == 'yes' and simple == True:
            print('Correct!')
            count_answer += 1
        elif answer.lower() == 'no' and simple == False:
            print('Correct!')
            count_answer += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{rand_num}'.")
            print(f"Let's try again, {name}!")
            break

    if count_answer == 3:
        print(f'Congratulations, {name}!')