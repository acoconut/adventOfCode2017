#!/usr/bin/python3
# Advent of code
# Day 10 - Part 1

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.read()
my_input = my_input.strip()
lengths = my_input.split(',')
lengths = [int(x) for x in lengths]

elements = list(range(256))
l = len(elements)

def get_sublist_to_hash(elements, length, current_position):

    if (current_position + length) >= l:
        tail_elements = l - current_position
        head_elements = length - tail_elements
        my_list = elements[current_position:]
        my_list.extend(elements[:head_elements])
        my_list.reverse()
        return [my_list[len(my_list)-head_elements:], my_list[:tail_elements]]
    else:
        my_list = elements[current_position:current_position+length]
        my_list.reverse()
        return [my_list]

def hash_list(elements, length, current_position):
    slices = get_sublist_to_hash(elements, length, current_position)
    if (len(slices) == 2):
        head_elements = len(slices[0])
        tail_elements = len(slices[1])
        num_elements = l - tail_elements - head_elements
        my_list = slices[0]
        my_list.extend(elements[head_elements:head_elements + num_elements])
        my_list.extend(slices[1])
    else:
        my_list = elements[:current_position]
        my_list.extend(slices[0])
        my_list.extend(elements[(current_position + length):])

    return my_list


skip = 0
current_position = 0
for length in lengths:
    elements = hash_list(elements, length, current_position)
    current_position = (current_position + length + skip) % l 
    skip += 1


print (elements[0] * elements[1])
