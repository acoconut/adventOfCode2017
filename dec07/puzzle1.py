#!/usr/bin/python3
# Advent of code
# Day 7 - Part 1

import re

# Read input
fo = open("input.txt", "r+")
my_input = list(fo)

class Tree:
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self.children = children

    def __str__(self):
        return str(' '.join([self.name, str(self.weight), str(self.children)]))

def getParent(line):
    [name, children] = line.split('->')
    children = children.split(',')
    children = [x.strip() for x in children]
    parent_name = re.findall(parent_name_regex, name)
    parent_name = parent_name[0].strip()
    value = re.findall(regex, line)
    return parent_name, int(value[0]), children

def getChild(line):
    value = re.findall(regex, line)
    child_name = line.split()[0]
    return child_name, int(value[0])

final = []
parents = []
seen_children = []
seen_parents = []
orphan_children = []
regex = re.compile(".*?\((.*?)\)")
parent_name_regex = re.compile("(.*?)\(")
for line in my_input:
    line = line.strip()
    if ("->" in line):
        [name, value, children] = getParent(line)
        parents.append((name, value, children))
        seen_parents.append(name)
        seen_children.extend(children)
    else:
        [name, value] = getChild(line)
        final.append((name, value))


print ([child for child in seen_parents if child not in seen_children])




        
