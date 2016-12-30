'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 7 Challenge 2
'''
import sys

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    reply = []
    for line in f:
    	reply.append(line)
    return reply

def is_aba(chars):
	a = chars[0]
	b = chars[1]
	if a == b:
		return False
	if a != chars[2]:
		return False

	return True

def rev_aba(chars):
	a = chars[1]
	b = chars[0]

	return a + b + a

def test_line(line):
	in_brackets = False
	test_str = ""
	found = []
	hypernet = []
	for char in line:
		if char == "[":
			in_brackets = True
			test_str = ""
		test_str += char
		if len(test_str) > 3:
			test_str = test_str[1:]
		if len(test_str) == 3:
			test = is_aba(test_str)
			if test:
				if in_brackets:
					hypernet.append(test_str)
				else:
					found.append(rev_aba(test_str)) 
		if char == "]":
			in_brackets = False
			test_str = ""

	for x in found:
		if x in hypernet:
			return True
	return False

instructions = process_input(sys.argv[1])
counter = 0
for line in instructions:
	if test_line(line):
		counter+=1

print counter