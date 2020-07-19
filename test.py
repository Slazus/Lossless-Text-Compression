from Huffman import *
from RLE_b import *
from LZ77 import *

import random

def openTextFile(i):
    with open('./testcases/' + i, 'r') as file:
        string = file.read()

    file.close()
    return string


def writeTextFile(i, data):
    with open('./output/'+ i + '.txt', 'w') as file:
        file.write(data)

    file.close()




def runTest():
    test = openTextFile('lorem_ipsum.txt')
    print(test)
    rle_compressed = RLE_encode(test)
    print(rle_compressed)
    writeTextFile("lorem_ipsum", rle_compressed)

    print("Original: " + str(len(test)) + " byte \tCompressed (RLE): " + str(len(rle_compressed)) + " byte")
    print('*' * 100)




#runTest()

string = 'AAAAAAAABBCDEEEEFFFFFGHILLLMNNNOOOOOOOOOPPPPPQQRRSSTUUUUVVVVXXYYYZZ'
ex = RLE_encode(string)
ex2 = Huffman_encode(string)
ex3 = LZ77_encode(string, 20, 10)

print('Input: ' + string)
print('Original size: ' + str(len(string)) + ' byte')
print('RLE size: ' + str(len(ex)) + ' byte')
print('Huffman size: ' + str(len(ex2[0])) + ' bit \t(' + str(int(len(ex2[0])/8)) + ' byte)')
print('LZ77 size: ' + str(len(ex3)) + ' byte')