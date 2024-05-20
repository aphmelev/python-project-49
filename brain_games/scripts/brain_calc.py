#!/usr/bin/env python3
import prompt
import brain_games.games.brain_calc as brain_calc


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    brain_calc.start(name)
