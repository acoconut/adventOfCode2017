#!/usr/bin/python3
# Advent of code
# Day 8 - Part 2

# Read input
fo = open("input.txt", "r+")
my_input = list(fo)

registers = {}

def apply_command(action, max_registers):
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

    current_max = max(registers.values())
    if (current_max > max_registers):
        max_registers = current_max
    return max_registers

max_registers = 0 
for line in my_input:
    line = line.strip()
    [action, condition] = line.split("if")

    [part1, operator, part2] = condition.split()
    part2 = int(part2)

    if (part1 not in registers):
        registers[part1] = 0

    if (operator == '>'):
        if (registers[part1] > part2):
            max_registers = apply_command(action, max_registers)
    elif (operator == '<'):
        if (registers[part1] < part2):
            max_registers = apply_command(action, max_registers)
    elif (operator == '>='):
        if (registers[part1] >= part2):
            max_registers = apply_command(action, max_registers)
    elif (operator == '<='):
        if (registers[part1] <= part2):
            max_registers = apply_command(action, max_registers)
    elif (operator == '=='):
        if (registers[part1] == part2):
            max_registers = apply_command(action, max_registers)
    elif (operator == '!='):
        if (registers[part1] != part2):
            max_registers = apply_command(action, max_registers)

print (max_registers)
