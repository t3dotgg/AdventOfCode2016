'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 4 Challenge 1
'''
import sys
import collections
import re

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    reply = []
    for line in f:
    	split = line.split('[')
    	split[1] = split[1][:5]
    	reply.append(split)
    return reply

def count_top_5(instruction):
	print instruction[0]
	characters = ''.join([i for i in instruction[0].replace('-', '') if not i.isdigit()])
	print characters
	counts = {}
	for letter in set(characters):
		count = characters.count(letter)
		if count in counts:
			counts[count] = ''.join(sorted(letter + counts[count]))
		else:
			counts[count] = letter
	# counts = collections.OrderedDict(sorted(counts))
	print counts
	# sorted_string = ''.join(k for k,v in counts)
	tuples = []
	for key, val in counts.items():
		tuples.append( (val, key) )
	sorted_string = ''
	for tup in sorted(tuples, key=lambda tup: tup[1], reverse=True):
		sorted_string += tup[0]

	sorted_string = sorted_string[:5]
	print sorted_string
	print "Checksum: %s \n" % instruction[1]
	if sorted_string[:5] == instruction[1]:
		return True
	else:
		return False

def get_room_num(r):
	data = r.split('-')
	return int(data[len(data)-1])

instructions = process_input(sys.argv[1])
roomnums = []
for instruction in instructions:
	if count_top_5(instruction):
		roomnums.append(get_room_num(instruction[0]))

print sum(roomnums)