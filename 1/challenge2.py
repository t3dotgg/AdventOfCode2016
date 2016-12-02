'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 1 Challenge 2
'''
import sys

# Takes in turning character and direction, returns new direction
def rotate(turn, direction):
	if turn == 'L':
		# Left turn defined as y = x and x = -y
		y = direction[0]
		x = 0 - direction[1]
	else:
		# Right turn defined as y = -x and x = y
		y = 0 - direction[0]
		x = direction[1]
	return [x, y]

# Takes in amount of moves, direction, and current location,
# returns new location
def move(amount, direction, location):
	x = location[0] + (direction[0] * amount)
	y = location[1] + (direction[1] * amount)
	return (x,y)

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    return f.readlines()[0].split(', ')

instructions = process_input(sys.argv[1])
direction = [0,1]
location = (0,0)
locations = [location]

for movement in instructions:
	turn = movement[0]
	direction = rotate(turn, direction)

	amount = int(movement[1:len(movement)])

	# Goes step by step for amount specified
	for x in range(0, amount):
		location = move(1, direction, location)

		# If location has been reached before
		if location in locations:
			distance = abs(location[0]) + abs(location[1])
			print "Found Easter Bunny HQ at (%i, %i), %i blocks away" % (location[0], location[1], distance)
			exit(0)

		# Append current location to list of locations
		locations.append(location)

# Sums absolute value of x and y, distance from origin (0,0)
print abs(location[0]) + abs(location[1])