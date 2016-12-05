'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 5 Challenge 1
'''
import sys
import md5

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    reply = []
    for line in f:
    	reply.append(line)
    return reply

index = 0
password = ""
instructions = process_input(sys.argv[1])
while len(password) != 8:
	m = md5.new()
	m.update(instructions[0] + str(index))
	hexed = m.hexdigest()
	if hexed[:5] == '00000':
		print "Found hex at %i" % index
		password += hexed[5]
	index += 1
print password