#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(finalLine):
  if invalid(finalLine):
    return "Too chaotic"
  return bubbleSort(finalLine)

def invalid(finalLine):
    return any(didBribeMoreThanTwoPeople(person, index) for index, person in enumerate(finalLine))

def didBribeMoreThanTwoPeople(person, index):
    return index + 2 < person - 1

def bubbleSort(line):
    swaps = 0
    numberOfPeople = len(line)

    for person in range(numberOfPeople):
        for i in range(0, numberOfPeople - person - 1):
            if line[i] > line[i + 1]:
                line[i], line[i + 1] = line[i + 1], line[i]
                swaps += 1

    return swaps


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
