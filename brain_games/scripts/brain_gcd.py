#!/usr/bin/env python3
import brain_games.games.brain_gcd as brain_gcd
import brain_games.scripts.brain_hello as hello


def main():
    brain_gcd.start(hello.hello())
