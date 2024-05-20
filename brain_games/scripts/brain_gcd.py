#!/usr/bin/env python3
import prompt
import brain_games.games.brain_gcd as brain_gcd


def gcd_fun(x, y):
    if y == 0:
        return x
    else:
        return gcd_fun(y, x % y)


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    brain_gcd.start(name)
