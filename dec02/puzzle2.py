#!/usr/bin/python3
# Advent of code
# Day 2 - Part 2
from itertools import combinations

# Read input
fo = open("input.txt", "r+")
my_input = list(fo)

total = 0
for line in my_input:
        
        line = line.rstrip()
        line = line.split()
        line = [int(x) for x in line]
        for i, j in list(combinations(line, 2)):
                if (i % j == 0):
                        total = total + (i/j)
                if (j % i == 0):
                        total = total + (j/i)
print (total)
        
