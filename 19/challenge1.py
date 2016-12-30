'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 19 Challenge 1
'''
import sys
import md5

num_elves = int(sys.argv[1])
elves = {}

binary = str(bin(num_elves)) # String representation of binary
binary = list(binary) # List of binary digits
binary[2] = 0 # Removes first digit from binary representation
binary = "".join(str(i) for i in binary) # Turns binary back into string
l = int(binary, 2) # Finally, turns binary string back into integer
print l # Prints the l value in 2^n + l
print 2 * l + 1 # Answer is 2l + 1
