#!/usr/bin/python3
# Advent of code
# Day 7 - Part 1

import re

# Read input
fo = open("input.txt", "r+")
my_input = list(fo)

# First lets separate children and parents
final = {}
parents = {}
regex = re.compile(".*?\((.*?)\)")
parent_name_regex = re.compile("(.*?)\(")
for line in my_input:
    line = line.strip()
    if ("->" in line):
        [name, children] = line.split('->')
        children = children.split(',')
        children = [x.strip() for x in children]
        value = re.findall(regex, name)
        parent_name = re.findall(parent_name_regex, name)
        parents[(parent_name, value)]=children 
    else:
        value = re.findall(regex, line)
        final[line.split()[0]] = int(value[0])

print (final)
print ('------')
print (parents)
# Second, lets build the tree
while (len(final) > 0):
    for parent in parents:
        children = parents[parent]
        for child in children:
            #if (child in parents):
            pass;
