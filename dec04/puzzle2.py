#!/usr/bin/python3
# Advent of code
# Day 4 - Part 1

# Read input
fo = open("input.txt", "r+")
my_input = list(fo)

cont = 0
for line in my_input:
        line = line.rstrip()
        words = line.split()
        original_size = len(words)
        unique_words = set(words)
        unique_size = len(unique_words)
        if (original_size == unique_size):
                no_anagrams = []
                for word in unique_words:
                        no_anagrams.append("".join(sorted(word)))
                        no_anagrams_size = len(set(no_anagrams))
                        if (no_anagrams_size == unique_size):
                                cont = cont + 1

print(cont)
