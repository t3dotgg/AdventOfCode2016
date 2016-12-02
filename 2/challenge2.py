'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 2 Challenge 1
'''
import sys

def move(dir, keypad, x, y):
	old_x = x
	old_y = y
	length = len(keypad)
	if dir == "U":
		y -= 1
	elif dir == "D":
		y += 1
	elif dir == "L":
		x -= 1
	elif dir == "R":
		x += 1

	if x < 0 or y < 0 or y >= length or x >= length:
		# Location out of bounds on keypad
		return (old_x, old_y)

	if keypad[y][x] == -1:
		# Location inaccessible on keypad
		return (old_x, old_y)

	return (x,y)

# Takes in input location and returns list of instructions
def process_input(file_location):
    f = open(file_location, "r")
    reply = []
    for line in f:
    	reply.append(line)
    return reply

x = 0
y = 2
N = -1

keypad = [  [  N ,  N ,  1  ,  N ,   N ],
			[  N ,  2 ,  3  ,  4 ,   N ],
			[  5 ,  6 ,  7  ,  8 ,   9 ],
			[  N , "A", "B" , "C",   N ],
			[  N ,  N , "D" ,  N ,   N ]]

answer = ""
instructions = process_input(sys.argv[1])

for row in instructions:
	for char in row:
		x, y = move(char, keypad, x, y)
	answer += str(keypad[y][x])

print answer