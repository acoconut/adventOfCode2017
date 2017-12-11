#!/usr/bin/python3
# Advent of code
# Day 9 - Part 2

# Read input
fo = open("input.txt", "r+")
my_input = fo.read()
my_input = my_input.strip()

def clean_input(my_input):
    garbage_counter = 0
    my_clean_input = ""
    skip_next = False
    open_garbage = False
    for char in my_input:
        if (not skip_next and not open_garbage):
            if char == '!':
                skip_next = True
            elif char == '<':
                open_garbage = True
            else:
                my_clean_input += char
        elif (not skip_next and open_garbage and char == '>'):
            open_garbage = False
        elif (not skip_next and open_garbage and char == '!'):
            skip_next = True
            continue
        elif (skip_next):
            skip_next = False
            continue
        elif (open_garbage):
            garbage_counter += 1

    return garbage_counter

print (clean_input(my_input))

