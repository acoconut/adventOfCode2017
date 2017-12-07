#!/usr/bin/python3
# Advent of code
# Day 6 - Part 2

# Read input
fo = open("input.txt", "r+")
my_input = fo.read().split("\t")

# Get input ready
memory = []
for number in my_input:
    number = number.strip()
    number = int(number)
    memory.append(number)

infinite_loop = False
l = len(memory)
seen_memories = {}
cont = 0
while (not infinite_loop):
    highest = max(memory)
    highest_index = memory.index(highest)
    memory[highest_index] = 0 

    for i in range(1,highest+1):
        index = (i+highest_index) % l
        memory[index] += 1
    
    memory_to_save = ''.join([str(number) for number in memory])
    cont += 1
    if (not memory_to_save in seen_memories):
        seen_memories[memory_to_save] = cont
    else:
        infinite_loop = True
        print (cont - seen_memories[memory_to_save])
