'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 7 Challenge 1
'''
import sys

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    reply = []
    for line in f:
    	reply.append(line)
    return reply

def is_abba(chars):
	a = chars[0]
	b = chars[1]
	if a == b:
		return False
	if a != chars[3]:
		return False
	if b != chars[2]:
		return False

	return True

def test_line(line):
	in_brackets = False
	test_str = ""
	found = False
	for char in line:
		if char == "[":
			in_brackets = True
			test_str = ""
		test_str += char
		if len(test_str) > 4:
			test_str = test_str[1:]
		if len(test_str) == 4:
			test = is_abba(test_str)
			if test:
				if in_brackets:
					print "Found abba in brackets, returning false"
					return False
				else:
					print "found ABBA outside of brackets"
					found = True
		if char == "]":
			in_brackets = False
			test_str = ""

	return found

instructions = process_input(sys.argv[1])
counter = 0
for line in instructions:
	if test_line(line):
		counter+=1

print counter