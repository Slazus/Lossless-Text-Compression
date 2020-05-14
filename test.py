from Huffman import *
from RLE import *
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


def randomString(length):
    l = ['a', 'b', 'c']

    string = ''
    while length > 0:
        c = random.choice(l)
        seq = c * random.randint(1, 10)
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



runTest(3)
