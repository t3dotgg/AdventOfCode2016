'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 6 Challenge 1
'''
import sys
import itertools
import operator

# Found at https://stackoverflow.com/questions/1518522/python-most-common-element-in-a-list
def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return min(groups, key=_auxfun)[0]

# Takes in input location and returns list of instructions
def process_input(file_location, charlists):
    f = open(file_location, "r")
    for line in f:
    	for x in range(len(line)):
    		print x
    		charlists[x].append(line[x])
    return charlists

charlists = [[] for i in range(9)]
charlists = process_input(sys.argv[1], charlists)

answer = [''] * 8
for x in range(8):
	answer[x] = most_common(charlists[x])

print answer