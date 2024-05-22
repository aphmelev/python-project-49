#!/usr/bin/env python3
import brain_games.games.brain_prime as brain_prime
import brain_games.scripts.brain_hello as hello


def main():
    brain_prime.start(hello.hello())
