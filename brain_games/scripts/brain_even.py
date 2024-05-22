#!/usr/bin/env python3
import brain_games.games.brain_even as brain_even
import brain_games.scripts.brain_hello as hello


def main():
    brain_even.start(hello.hello())
