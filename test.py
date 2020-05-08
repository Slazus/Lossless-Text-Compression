from Huffman import *
from RLE import *

def LoadInputText(i):
    with open('./test/input' + str(i) + '.txt', 'r') as file:
        string = file.read()

    file.close()
    return string


def RunTest(i):
    test = LoadInputText(i)
    print(test)
    compressed = RLE_encode(test)
    print(compressed)

    print("Original: " + str(len(test)) + " byte \tCompressed (RLE): " + str(len(compressed)) + " byte")
    print('*' * 100)

    compressed = HUFFMAN_encode(test)
    print(compressed)
    print("Original: " + str(len(test)) + " byte \tCompressed (HUFFMAN): " + str(int(len(compressed) / 8)) + " byte")   


RunTest(2)


