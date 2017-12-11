#!/usr/bin/python3
# Advent of code
# Day 8 - Part 1

# Read input
fo = open("input.txt", "r+")
my_input = list(fo)

registers = {}

def apply_command(action):
    [part_action1, command, part_action2] = action.split()
    part_action2 = int(part_action2)

    increment = False
    if (command == "inc"):
        increment = True
    if (part_action1 not in registers):
        registers[part_action1] = 0 

    if (increment):
        registers[part_action1]+= int(part_action2)
    else:
        if (part_action2 < 0):
            registers[part_action1] += abs(part_action2)
        else:
            registers[part_action1] -= part_action2

for line in my_input:
    line = line.strip()
    [action, condition] = line.split("if")

    [part1, operator, part2] = condition.split()
    part2 = int(part2)

    if (part1 not in registers):
        registers[part1] = 0

    if (operator == '>'):
        if (registers[part1] > part2):
            apply_command(action)
    elif (operator == '<'):
        if (registers[part1] < part2):
            apply_command(action)
    elif (operator == '>='):
        if (registers[part1] >= part2):
            apply_command(action)
    elif (operator == '<='):
        if (registers[part1] <= part2):
            apply_command(action)
    elif (operator == '=='):
        if (registers[part1] == part2):
            apply_command(action)
    elif (operator == '!='):
        if (registers[part1] != part2):
            apply_command(action)

print (max(registers.values()))

