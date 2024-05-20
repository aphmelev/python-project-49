#!/usr/bin/env python3
import prompt
import brain_games.games.brain_prime as brain_prime


def is_simple(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    brain_prime.start(name)
