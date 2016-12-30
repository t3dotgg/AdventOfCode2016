'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 8 Challenge 2
'''
import sys

height = 6
width = 50

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    reply = []
    for line in f:
    	reply.append(line.split())
    return reply

def empty_pad(wi, he):
	result = []
	for h in range(he):
		row = []
		for w in range(wi):
			row.append('.')
		result.append(row)
	return result

def shift_row(pad, row, amount):
	new_row = ['.'] * width
	for i in range(width):
		print "Shifting %i to %i" % (i, (i+amount) % width)
		new_row[(i+amount) % width] = pad[row][i]
	pad[row] = new_row
	return pad

def shift_column(pad, column, amount):
	new_col = ['.'] * height
	for i in range(height):
		new_col[(i+amount) % height] = pad[i][column]

	for i in range(height):
		pad[i][column] = new_col[i]
	return pad

def count_pad(pad):
	counter = 0
	for x in range(width):
		for y in range(height):
			if pad[y][x] == '#':
				counter+=1
	return counter

def fill_rect(pad, x, y):
	for i in range(y):
		for b in range(x):
			pad[i][b] = '#'

	return pad

def print_pad(pad):
	for y in range(height):
		line = ''
		for x in range(width):
			line+= pad[y][x]
		print line

instructions = process_input(sys.argv[1])

pad = empty_pad(width, height)

for instruction in instructions:
	if instruction[0] == "rotate":
		if instruction[1] == "row":
			row = int(instruction[2][2:])
			count = int(instruction[4])
			pad = shift_row(pad, row, count)
		if instruction[1] == "column":
			column = int(instruction[2][2:])
			count = int(instruction[4])
			pad = shift_column(pad, column, count)
	if instruction[0] == "rect":
		sides = instruction[1].split('x')
		x = int(sides[0])
		y = int(sides[1])
		print "Filling rect for %i, %i" % (x, y)
		pad = fill_rect(pad, x, y)

	print_pad(pad)

print(count_pad(pad))