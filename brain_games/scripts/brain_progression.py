#!/usr/bin/env python3
import brain_games.games.brain_progression as brain_progression
import brain_games.scripts.brain_hello as hello


def main():
    brain_progression.start(hello.hello())
