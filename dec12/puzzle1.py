#!/usr/bin/python3
# Advent of code
# Day 12 - Part 1

# Read input
with open("input.txt", "r") as fo:
    programs_definitions = {}
    for line in fo:
        line = line.strip()
        (name, connections) = line.split(' <-> ')
        connections = [x.strip() for x in connections.split(',')]
        programs_definitions[name] = connections

visited_programs = set()

def visit_program(programs_definitions, program, programs_to_visit):
    connections = None
    for name in programs_definitions:
        if name == program:
            connections = programs_definitions[name]
            break
    for connection in connections:
        if (connection not in visited_programs):
            programs_to_visit.append(connection)
    return programs_to_visit

programs_to_visit = ['0']


while (len(programs_to_visit) > 0):
    print (visited_programs, programs_to_visit)
    program = programs_to_visit.pop()
    programs_to_visit = visit_program(programs_definitions, program, programs_to_visit)
    if program not in visited_programs:
        visited_programs.add(program)


print (len(visited_programs))
