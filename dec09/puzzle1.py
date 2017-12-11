#!/usr/bin/python3
# Advent of code
# Day 9 - Part 1

# Read input
fo = open("input.txt", "r+")
my_input = fo.read()
my_input = my_input.strip()

def clean_input(my_input):
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
        else:
            skip_next = False
            continue

    return my_clean_input

def get_score(my_input):
    score = 0
    num_open_brackets = 0
    for char in my_input:
        if char == '{':
            num_open_brackets += 1
            score += num_open_brackets
        elif char == '}':
            num_open_brackets -= 1
    return score

my_clean_input = clean_input(my_input)
print (get_score(my_clean_input))

