from RLE import *
from Huffman import Huffman_encode, Huffman_decode
from LZ77 import LZ77_encode, LZ77_decode

import sys, os


if len(sys.argv) < 3:
    print("Wrong number of arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    WINDOW_SIZE = sys.argv[3]
else:
    WINDOW_SIZE = 256


FILENAME = sys.argv[1]
METHOD = sys.argv[2].upper()
WITHOUT_EXTENSION = FILENAME.split('.')[0]
WINDOW_SIZE_STRING = ''
EXTRA_SIZE = 0

file = open('./test/' + FILENAME, 'rb')

tic = time.perf_counter()

if METHOD == 'RLE':
    encoded = RLE_encode(file)
elif METHOD == 'HUFFMAN':
    encoded = Huffman_encode(file)
elif METHOD == 'LZ77':
    encoded = LZ77_encode(file.read(), WINDOW_SIZE)

toc = time.perf_counter()
time1 = toc-tic
file.close()


#Se sto usando Huffman devo considerare nella misura della dimensione anche
#la dimensione della tabella 
if METHOD == 'HUFFMAN':
    EXTRA_SIZE = os.stat('./test/table.huff').st_size
elif METHOD == 'LZ77':
    WINDOW_SIZE_STRING = '__' + str(WINDOW_SIZE)


compressed_filename = './test/' + WITHOUT_EXTENSION + WINDOW_SIZE_STRING + '.' + METHOD.lower()
output_compressed = open(compressed_filename, 'wb')
output_compressed.write(encoded)
output_compressed.close()

input_compressed = open(compressed_filename, 'rb')

tic = time.perf_counter()
if METHOD == 'RLE':
    decoded = RLE_decode(input_compressed)
elif METHOD == 'HUFFMAN':
    decoded = Huffman_decode(input_compressed)
elif METHOD == 'LZ77':
    decoded = LZ77_decode(input_compressed, WINDOW_SIZE)

toc = time.perf_counter()
time2 = toc-tic

decoded_file = open('./test/uncompressed_'+ METHOD + '__' + FILENAME, 'wb')
decoded_file.write(decoded)
decoded_file.close()
input_compressed.close()

compressed_size = len(encoded) + EXTRA_SIZE

print('_' * 100)
print('Original size: ' + str(len(decoded)) + ' bytes')
print('Compressed size (' + METHOD + '): ' + str(compressed_size) + ' bytes\n' )
print('Compression ratio: ' + '{:.2f}'.format(len(decoded)/compressed_size))
print('Space savings: ' +  '{:.2f}'.format((1 - (compressed_size/len(decoded)))* 100) + ' %\n')
print('Compression time: ' + '{:.4f}'.format(time1))
print('Uncompression time: ' + '{:.4f}'.format(time2))
print('_' * 100)