from Huffman import *
from RLE import *
from LZ77 import *

import random

def openTextFile(i):
    with open('./test/input' + str(i) + '.txt', 'r') as file:
        string = file.read()

    file.close()
    return string


def writeTextFile(i, data):
    with open('./test/output' + str(i) + '.txt', 'w') as file:
        file.write(data)

    file.close()


def randomString(length, charList):
    string = ''
    while length > 0:
        c = random.choice(charList)
        seq = c * random.randint(0, 2)
        string += seq
        length -= len(seq)

    return string


def runTest(i):
    test = openTextFile(i)
    print(test)
    compressed = RLE_encode(test)
    print(compressed)
    writeTextFile(i, compressed)

    print("Original: " + str(len(test)) + " byte \tCompressed (RLE): " + str(len(compressed)) + " byte")
    print('*' * 100)

    compressed_pair = Huffman_encode(test)
    compressed = compressed_pair[0]
    table = compressed_pair[1]
    print(compressed)
    print(table)
    print("Original: " + str(len(test)) + " byte \tCompressed (HUFFMAN): " + str(int(len(compressed) / 8)) + " byte")   
    uncompressed = Huffman_decode(compressed, table)
    print(uncompressed)

    if uncompressed == test:
        print("Matching!")



#runTest(3)

#string = 'abaababaabbaabbbbbbbbb'
#string = randomString(random.randint(0, 10), charList)
#string = 'ccbbcaccccbbacc' * 3
#string = 'cabracadabrarrarrad'

'''
charList = ['a', 'b', 'c']
string = randomString(10, charList)
string = 'a' * 10

#  TODO FIX THIS CASE for Huffman encoding
#  string = '' and string = 'a'

print("INPUT: " + string)

rle_encoded = RLE_encode(string)
huff_encoded = Huffman_encode(string)
lz77_encoded = LZ77_encode(string, 6, 7)

print("RLE Encoding: " + rle_encoded)
print("Huffman Encoding: " + str(huff_encoded))
print("LZ77 Encoding: \n" + lz77_encoded)
'''


'''
with open("./file.png", 'rb') as file:
    string = file.read()

file.close()

print(str(string))
a = LZ77_encode(str(string), 6, 7)
print(a)

b = LZ77_decode(a)
print('*' * 50)
print(b)

with open('./output.png', 'wb') as file:
    ss = str(string)
    kek = ss.encode()
    print(type(kek))
    file.write(kek)

file.close()
'''
