'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 14 Challenge 2
'''
import sys
import md5

def next_thousand(salt, thousand_index, char):
	location = thousand_index
	while location < thousand_index +999:
		location += 1
		hexed = sums[location]
		if char_repeated(hexed, 5, char):
			print "THOUSAND: Row of 5 at %i in %s" % (location, hexed)
			return location
	return False

def chars_repeated(hexed, amount):
	count = 1
	for i in range(1,len(hexed)):
		if hexed[i] == hexed[i-1]:
			count+=1
		else:
			count = 1
		if count == amount:
			return hexed[i]
	return False

def extra_hexer(tohex, amount = 2017):
	hexed = tohex
	for i in range(amount):
		m = md5.new()
		m.update(hexed)
		hexed = m.hexdigest()
	return hexed

def char_repeated(hexed, amount, char):
	count = 0
	for i in range(len(hexed)):
		if hexed[i] == char:
			count+=1
		else:
			count = 0
		if count == amount:
			return True
	return False

def generate_sums(sums, salt, start, finish = None):
	if finish == None:
		finish = start + 1000
	for i in range(start, finish):
		sums.append(extra_hexer(salt + str(i)))
	return sums

salt = sys.argv[1]
sums = generate_sums([], salt, 0)
index = 0
keys = []

while len(keys) < 64:
	if index > len(sums):
		print "needs more sums"
		sums = generate_sums(sums, salt, index)
	hexed = sums[index]
	if chars_repeated(hexed, 3):
		print "Row of 3 in %s" % hexed
		# Match, check for 5 repeat in next 1000
		char = chars_repeated(hexed, 3)
		while len(sums) < index + 1000:
			sums = generate_sums(sums, salt, len(sums))
		if next_thousand(sums, index, char):
			keys.append(index)
	index+=1

print keys