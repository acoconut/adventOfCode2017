#!/usr/bin/python3
# Advent of code
# Day 12 - Part 1

# Read input
fo = open("input.txt", "r+")
programs_definitions = []
for line in fo:
    line = line.strip()
    [name, connections] = line.split(' <-> ')
    connections = connections.split(',')
    connections = [x.strip() for x in connections]
    programs_definitions.append((name, connections))

visited_programs = []

def visit_program(programs_definitions, program, programs_to_visit):
    connections = [x[1] for x in programs_definitions if x[0] == program]
    for connection in connections[0]:
        if connection not in visited_programs and connection not in programs_to_visit:
            programs_to_visit.append(connection)
    return programs_to_visit

programs_to_visit = ['0']


while (len(programs_to_visit) > 0):
    print (visited_programs, programs_to_visit)
    program = programs_to_visit.pop()
    programs_to_visit = visit_program(programs_definitions, program, programs_to_visit)
    visited_programs.append(program)

print (len(visited_programs))
