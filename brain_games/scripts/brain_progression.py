#!/usr/bin/env python3
import prompt
import brain_games.games.brain_progression as brain_progression


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    brain_progression.start(name)
