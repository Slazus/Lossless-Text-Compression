from Huffman import *
from RLE import *

def OpenTextFile(i):
    with open('./test/input' + str(i) + '.txt', 'r') as file:
        string = file.read()

    file.close()
    return string

def WriteTextFile(i, data):
    with open('./test/output' + str(i) + '.txt', 'w') as file:
        file.write(data)

    file.close()


def RunTest(i):
    test = OpenTextFile(i)
    print(test)
    compressed = RLE_encode(test)
    print(compressed)
    WriteTextFile(i, compressed)

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



RunTest(3)