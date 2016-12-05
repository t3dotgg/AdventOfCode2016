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
found = 0
N = None
password = [N,N,N,N,N,N,N,N]
instructions = process_input(sys.argv[1])
while found != 8:
	m = md5.new()
	m.update(instructions[0] + str(index))
	hexed = m.hexdigest()
	if hexed[:5] == '00000':
		print "Found hex %s at %i" % (hexed, index)
		location = hexed[5]
		if location.isdigit() and int(location) < 8:
			location = int(location)
			if password[location] == None:
				print "Adding character to location %i " % location
				found+=1
				password[location] = str(hexed[6]) 
	index += 1
password = "".join(password)
print password