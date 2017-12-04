#!/usr/bin/python3
# Advent of code
# Day 3 - Part 1

import numpy as np

def get_value(matrix, x, y):
    if (x < 0) or (y < 0):
        return 0
    try:
        n = matrix[x][y]
        return n 
    except IndexError:
        return 0

def sum_surroundings(matrix, coor):
    x = int(coor[0])
    y = int(coor[1])

    return (get_value(matrix, x-1, y-1) + get_value(matrix, x-1, y) + get_value(matrix, x-1, y+1) + get_value(matrix, x, y-1) + get_value(matrix, x, y+1) + get_value(matrix, x+1, y-1) + get_value(matrix, x+1, y) + get_value(matrix, x+1, y+1))

def create_matrix(number):
    matrix=[[5, 4, 3], [6, 1, 2], [7, 8, 9]] #initial matrix
    empty_matrix=[[0, 0, 0], [0, 1, 0], [0, 0, 0]] #initial matrix
    max_number = 9

    while (max_number < number):
        l = len(matrix)
        max_number = matrix[l-1][l-1]
        #Right side
        for i in range(l):
            max_number = max_number + 1
            matrix[l-i-1].append(max_number) 
            empty_matrix[l-i-1].append(0) 

        #Top side
        row = []
        empty_row=[]
        for i in range(l+1):
            #First create row
            max_number = max_number + 1
            row.append(max_number)
            empty_row.append(0)
        #Then insert it
        matrix.insert(0, row[::-1])
        empty_matrix.insert(0, empty_row)

        #Left side
        for line in matrix:
            max_number = max_number + 1
            line.insert(0, max_number)
        for line in empty_matrix:
            line.insert(0, 0)

        #Bottom side
        row = []
        empty_row = []
        for i in range(l+2):
            max_number = max_number + 1
            row.append(max_number)
            empty_row.append(0)
        matrix.append(row)
        empty_matrix.append(empty_row)

    return (matrix, empty_matrix)

def fill_matrix (matrix, empty_matrix, number):
    matrix = np.array(matrix)
    surroundings = 0
    cont = 2

    while (number > surroundings):
        coor = np.where(matrix==cont)
        surroundings = sum_surroundings(empty_matrix, (coor[0], coor[1]))
        empty_matrix[int(coor[0])][int(coor[1])] = surroundings
        cont = cont + 1
    print ("Result: " + str(surroundings))
    return empty_matrix 

#My input
number = 277678

matrix, empty_matrix = create_matrix(number)
new_matrix = fill_matrix(matrix, empty_matrix, number)

