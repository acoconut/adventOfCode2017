#!/usr/bin/python3
# Advent of code
# Day 11 - Part 2

class Hexmatrix:
    
    def __init__(self):
        self.north = 0
        self.west = 0

    def move(self, direction):
        if (direction == 'nw'):
            self.north += 0.5
            self.west += 0.5
        elif (direction == 'ne'):
            self.north += 0.5
            self.west -= 0.5
        elif (direction == 'sw'):
            self.north -= 0.5
            self.west += 0.5
        elif (direction == 'se'):
            self.north -= 0.5
            self.west -= 0.5
        elif (direction == 'n'):
            self.north += 1
        elif (direction == 's'):
            self.north -= 1
        elif (direction == 'w'):
            self.west += 1
        elif (direction == 'e'):
            self.west -= 1

    def calculate_distance(self):
        return abs(self.north) + abs(self.west)

fo = open("input.txt", 'r+')
my_input = fo.read()
my_input = my_input.strip()
directions = my_input.split(',')

furthest = 0
matrix = Hexmatrix()
for direction in directions:
    matrix.move(direction)
    distance = matrix.calculate_distance()
    if (distance > furthest):
        furthest = distance

print (furthest)
