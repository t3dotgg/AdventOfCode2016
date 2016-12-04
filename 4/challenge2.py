'''
Theo Browne
Advent of Code
www.adventofcode.com
Day 4 Challenge 1
'''
import sys
import collections

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
    characters = ''.join([i for i in instruction[0].replace('-', '') if not i.isdigit()])
    counts = {}
    for letter in set(characters):
        count = characters.count(letter)
        if count in counts:
            counts[count] = ''.join(sorted(letter + counts[count]))
        else:
            counts[count] = letter
    tuples = []
    for key, val in counts.items():
        tuples.append( (val, key) )
    sorted_string = ''
    for tup in sorted(tuples, key=lambda tup: tup[1], reverse=True):
        sorted_string += tup[0]

    sorted_string = sorted_string[:5]
    if sorted_string[:5] == instruction[1]:
        return True
    else:
        return False

def caesar(plaintext,shift):

    # Make text from input "readable", no ints or dashes
    plaintext = ''.join([i for i in plaintext.replace('-', ' ') if not i.isdigit()])

    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    # Create our substitution dictionary
    dic={}
    for i in range(0,len(alphabet)):
        dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

    # Convert each letter of plaintext to the corrsponding
    # encrypted letter in our dictionary creating the cryptext
    ciphertext=""
    for l in plaintext.lower():
        if l in dic:
            l=dic[l]
        ciphertext+=l

    return ciphertext

def get_room_num(r):
    data = r.split('-')
    return int(data[len(data)-1])

instructions = process_input(sys.argv[1])
roomnums = []
for instruction in instructions:
    if count_top_5(instruction):
        roomnum = (get_room_num(instruction[0]))
        decrypt = caesar(instruction[0], roomnum)
        if decrypt.find("north") != -1:
            print "Room: %i, named %s" % (roomnum, decrypt)