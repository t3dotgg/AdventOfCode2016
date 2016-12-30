'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 14 Challenge 1
'''
import sys
import md5

def next_thousand(salt, thousand_index, char):
	location = thousand_index
	while location < thousand_index +1000:
		location += 1
		m = md5.new()
		m.update(salt + str(location))
		hexed = m.hexdigest()
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

salt = sys.argv[1]
index = 0
keys = []

while len(keys) < 64:
	m = md5.new()
	m.update(salt + str(index))
	hexed = m.hexdigest()
	if chars_repeated(hexed, 3):
		print "Row of 3 in %s" % hexed
		# Match, check for 5 repeat in next 1000
		char = chars_repeated(hexed, 3)
		if next_thousand(salt, index, char):
			keys.append(index)
	index+=1

print keys