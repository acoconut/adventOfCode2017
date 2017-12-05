#!/usr/bin/python3
# Advent of code
# Day 5 - Part 1

# Read input
fo = open("input.txt", "r+")
my_input = []
for line in fo:
    my_input.append(int(line.strip()))

place = 0 
l = len(my_input)
cont = 0


while (0 <= place < l):
    offset = my_input[place] 
    new_place = place + offset
    my_input[place] += 1
    cont += 1
    place = new_place

print (cont)


