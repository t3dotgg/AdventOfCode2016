'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 2 Challenge 1
'''
import sys

def move(dir, x, y):	
	old_x = x
	old_y = y
	length = 3
	if dir == "U":
		y -= 1
	elif dir == "D":
		y += 1
	elif dir == "L":
		x -= 1
	elif dir == "R":
		x += 1

	if x < 0 or y < 0 or y == length or x == length:
		# Location out of bounds on keypad
		return (old_x, old_y)

	return (x,y)

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    reply = []
    for line in f:
    	reply.append(line)
    return reply

x = 1
y = 1

keypad = [  [1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]]
answer = ""
instructions = process_input(sys.argv[1])

for row in instructions:
	for char in row:
		location = move(char, x, y)
		x = location[0]
		y = location[1]
	answer += str(keypad[y][x])

print answer