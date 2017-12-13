#!/usr/bin/python3
# Advent of code
# Day 12 - Part 2

# Read input
with open("input.txt", "r") as fo:
    programs_definitions = {}
    for line in fo:
        line = line.strip()
        (name, connections) = line.split(' <-> ')
        connections = [x.strip() for x in connections.split(',')]
        programs_definitions[name] = connections

l = len(programs_definitions)

def visit_program(programs_definitions, program, programs_to_visit, visited_programs):
    if (program in programs):
        programs.remove(program)
    connections = None
    for name in programs_definitions:
        if name == program:
            connections = programs_definitions[name]
            break
    for connection in connections:
        if (connection not in visited_programs):
            programs_to_visit.append(connection)
    return programs_to_visit

def find_group(programs):
    visited_programs = set() 
    initial_program = programs.pop()
    programs_to_visit = [initial_program]
    while (len(programs_to_visit) > 0):
        program = programs_to_visit.pop()
        programs_to_visit = visit_program(programs_definitions, program, programs_to_visit, visited_programs)
        if program not in visited_programs:
            visited_programs.add(program)
    return programs

programs = []
for program_definition in programs_definitions:
    programs.append(program_definition)

cont = 0
while (len(programs)>0):
    programs = find_group(programs)

    cont += 1

print (cont)
