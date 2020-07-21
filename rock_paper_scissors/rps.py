#!/usr/bin/python

import sys

POSSIBLE_MOVES = ["rock", "paper", "scissors"]
def rock_paper_scissors(n):
    possible_plays = []
    indices = [0] * n
    while True:
        possible_plays.append([POSSIBLE_MOVES[i] for i in indices])
        for i in range(len(indices)-1, -2, -1):
            if i == -1:
                return possible_plays
            indices[i] += 1
            if indices[i] >= len(POSSIBLE_MOVES):
                indices[i] = 0
                continue
            break

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
