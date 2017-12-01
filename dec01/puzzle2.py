#!/usr/bin/python3
# Advent of code
# Day 1 - Part 1

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.read().rstrip()
#my_input = my_input + my_input[0]

def mysum(numbers):
    length = len(numbers)
    half = length/2
    half_number = numbers[half]
    cont = 0
    total = 0
    for num in numbers:
        if (half_number == num):
	    total = total + int(num)
        cont = cont + 1
        index = (half+cont)%len(numbers)
        half_number = numbers[index]
    return total

print(mysum(list(my_input)))
