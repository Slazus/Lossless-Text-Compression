from Huffman import *
from RLE import *
from bLZ77 import *

import random, os

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
os.remove("./compressed")
os.remove("./uncompressed")
'''

with open("./file", 'rb') as file:
    data = file.read()
file.close()

a = LZ77_encode(data, 600, 500)

a = a.replace(',', '')
a = a.replace('(', '')
a = a.replace(')', '')

with open("./compressed", 'w') as file:
    file.write(a)
file.close()

print("DONE")

'''
with open("./compressed", 'r') as file:
    k = file.read()
file.close()

b = LZ77_decode(k)

with open("./uncompressed", 'wb') as file:
    file.write(b)
file.close()

print("DONE")

print(str(string))

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
