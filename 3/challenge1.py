'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 3 Challenge 1
'''
import sys

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    reply = []
    for line in f:
    	reply.append(line.split())
    return reply

def is_triangle(line):
	ints = [int(line[0]), int(line[1]), int(line[2])]
	maximum = max(ints)
	ints.remove(maximum)
	if ints[0] + ints[1] > maximum:
		return True
	return False

possible = 0
instructions = process_input(sys.argv[1])

for line in instructions:
	if is_triangle(line):
		possible +=1

print possible