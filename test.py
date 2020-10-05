from RLE import *
from Huffman import Huffman_encode, Huffman_decode
from LZ77 import LZ77_encode, LZ77_decode
import sys, os, time

#Verifica del numero di argomenti ed eventuale messaggio di usage
if len(sys.argv) < 3:
    print("\nUsage: python test.py fileInTestFolder COMPRESSION_METHOD WINDOW_SIZE")
    print("-COMPRESSION_METHOD = RLE | HUFFMAN | LZ77\n-WINDOW_SIZE is only required for LZ77, if not specified the default size is 256\n")
    sys.exit(1)
#Parsing di WINDOW_SIZE o eventuale scelta del valore di default      
elif len(sys.argv) > 3:
    WINDOW_SIZE = int(sys.argv[3])
else:
    WINDOW_SIZE = 256

#Parsing degli argomenti da terminare e inizializzazione di variabili
FILENAME = sys.argv[1]
METHOD = sys.argv[2].upper()
WITHOUT_EXTENSION = FILENAME.split('.')[0]
WINDOW_SIZE_STRING = ''
EXTRA_SIZE = 0

#Apro il file in lettura
file = open('./test/' + FILENAME, 'rb')

#Faccio partire il timer
tic = time.perf_counter()

#Verifico il metodo di compressione e lo utilizzo a mia volta
if METHOD == 'RLE':
    encoded = RLE_encode(file)
elif METHOD == 'HUFFMAN':
    encoded = Huffman_encode(file)
else:
    encoded = LZ77_encode(file, WINDOW_SIZE)

#Fermo il timer
toc = time.perf_counter()

#Calcolo il tempo trascorso
compression_time = toc-tic

#Chiudo il file
file.close()


#Se sto usando Huffman devo considerare nella misura della dimensione anche
#la dimensione della tabella, se uso LZ77 il mio file decompresso avra' un nome diverso
#che indica la WINDOW_SIZE utilizzata
if METHOD == 'HUFFMAN':
    EXTRA_SIZE = os.stat('./test/table.huff').st_size
elif METHOD == 'LZ77':
    WINDOW_SIZE_STRING = '__' + str(WINDOW_SIZE)

#Procedo col salvataggio del file 
compressed_filename = './test/' + WITHOUT_EXTENSION + WINDOW_SIZE_STRING + '.' + METHOD.lower()
output_compressed = open(compressed_filename, 'wb')
output_compressed.write(encoded)
output_compressed.close()


#Conclusa la fase di compressione, procedo con l'apertura del file compresso per
#iniziare i test di decompressione
input_compressed = open(compressed_filename, 'rb')

#Faccio partire il timer
tic = time.perf_counter()

#Verifico nuovamente il metodo di compressione e scelgo il relativo algoritmo
#di decodifica
if METHOD == 'RLE':
    decoded = RLE_decode(input_compressed)
elif METHOD == 'HUFFMAN':
    decoded = Huffman_decode(input_compressed)
else:
    decoded = LZ77_decode(input_compressed, WINDOW_SIZE)

#Fermo il timer
toc = time.perf_counter()

#Calcolo il tempo trascorso
uncompression_time = toc-tic

#Apro il file in scrittura e procedo con l'esportazione
decoded_file = open('./test/uncompressed_'+ METHOD + '__' + FILENAME, 'wb')
decoded_file.write(decoded)
decoded_file.close()
input_compressed.close()

#Calcolo la dimensione del file, contando eventualmente anche la dimensione extra
#introdotta dalla tabella di Huffman
compressed_size = len(encoded) + EXTRA_SIZE


#Stampo il risultato dei test
print('_' * 100)
print('Original/uncompressed size: ' + str(len(decoded)) + ' bytes')
print('Compressed size (' + METHOD + '): ' + str(compressed_size) + ' bytes\n' )
print('Compression ratio: ' + '{:.2f}'.format(len(decoded)/compressed_size))
print('Space savings: ' +  '{:.2f}'.format((1 - (compressed_size/len(decoded)))* 100) + ' %\n')
print('Compression time: ' + '{:.4f}'.format(compression_time) + " seconds")
print('Uncompression time: ' + '{:.4f}'.format(uncompression_time) + " seconds")
print('_' * 100)