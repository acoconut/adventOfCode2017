#!/usr/bin/python3
# Advent of code
# Day 3 - Part 1

import numpy as np

def create_matrix(number):
    matrix=[[5, 4, 3], [6, 1, 2], [7, 8, 9]] #initial matrix
    max_number = 9

    while (max_number < number):
        l = len(matrix)
        max_number = matrix[l-1][l-1]
        #Right side
        for i in range(l):
            max_number = max_number + 1
            matrix[l-i-1].append(max_number) 

        #Top side
        row = []
        for i in range(l+1):
            #First create row
            max_number = max_number + 1
            row.append(max_number)
        #Then insert it
        matrix.insert(0, row[::-1])

        #Left side
        for line in matrix:
            max_number = max_number + 1
            line.insert(0, max_number)

        #Bottom side
        row = []
        for i in range(l+2):
            max_number = max_number + 1
            row.append(max_number)
        matrix.append(row)

    return matrix


#My input
number = 277678

matrix = create_matrix(number)

#Print matrix 
for line in matrix:
    print (line)
    
numpy_matrix = np.array(matrix)
initial_coor = np.where(numpy_matrix==1)
mynum_coor = np.where(numpy_matrix==number)

steps_x = initial_coor[0] - mynum_coor[0]
steps_y = initial_coor[1] - mynum_coor[1]

print ("Answer: " + str(abs(steps_x) + abs(steps_y)))
