#!/usr/bin/python3
# Advent of code
# Day 2 - Part 1

# Read input
fo = open("input.txt", "r+")
my_input = list(fo)

total = 0
for line in my_input:
        line = line.rstrip()
        line = line.split()
        line = [int(x) for x in line]
        max_num = max(line)
        min_num = min(line)
        total = total + int(max_num) - int(min_num)
print (total)
        
