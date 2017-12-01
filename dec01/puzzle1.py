#!/usr/bin/python3
# Advent of code
# Day 1 - Part 1

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.read().rstrip()
my_input = my_input + my_input[0]

def mysum(numbers):
	prev_number = 0 
	total = 0
	for num in numbers:
		if (prev_number == num):
			total = total + int(num)
		prev_number = num
	return total

print(mysum(list(my_input)))
