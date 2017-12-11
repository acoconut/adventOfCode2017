#!/usr/bin/python3
# Advent of code
# Day 7 - Part 2

import re
from collections import Counter

# Read input
fo = open("input.txt", "r+")
my_input = list(fo)
number_of_nodes = len(my_input)

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


calculated_score = []
calculated_score.extend(final)

def calculate_scores():
    for parent in parents:
        [parent_to_check, score, children] = parent
        if any(parent_to_check in iter_parent for iter_parent in calculated_score):
            continue
        total_score = score
        scored = True
        for child in children:
            if any(child in iter_children for iter_children in calculated_score):
                name_value = [x for x in calculated_score if child in x]
                name = name_value[0][0]
                value = name_value[0][1]
                total_score += value
            else:
                scored = False 
        if (scored):
            calculated_score.append((parent_to_check, total_score))

while (len(calculated_score) < number_of_nodes):
    calculate_scores()

for parent in parents:
    [parent_name, score, children] = parent
    children_scores = []
    children_name_scores = []
    for child in children:
       child_score = [x for x in calculated_score if child in x]
       children_scores.append(child_score[0][1])
       children_name_scores.extend(child_score)
    if (len(set(children_scores)) != 1):
        scores = Counter(children_scores)
        scores = list(scores.most_common())
        bad_score = scores[-1][0]
        good_score = scores[0][0]
        units_to_remove = bad_score - good_score
        bad_disc = [x for x in children_name_scores if bad_score in x][0][0]
        bad_disc_score = [x for x in parents if bad_disc in x][0][1]
        print (bad_disc_score - (bad_score - good_score))
        break
