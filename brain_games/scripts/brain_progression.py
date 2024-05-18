#!/usr/bin/env python3
import random
import prompt

def progression(start, step, count):
    lst = []
    for _ in range(count):
        lst.append(start + step)
        start = start + step
    return lst


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count_answer = 0

    for _ in range(3):
        lst = progression(random.randint(1, 11), random.randint(1, 11), random.randint(5, 11))
        rand_lst = random.choice(lst)

        for i in range(len(lst)):
            if lst[i] == rand_lst:
                lst[i] = '..'

        print(f'Question: {" ".join(map(str, lst))}')
        answer = prompt.string('Your answer: ')


        if answer == str(rand_lst):
            print('Correct!')
            count_answer += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{rand_lst}'.")
            print(f"Let's try again, {name}!")
            break

    if count_answer == 3:
        print(f'Congratulations, {name}!')