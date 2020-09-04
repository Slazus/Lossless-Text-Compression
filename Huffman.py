from queue import PriorityQueue 
from bitarray import bitarray

'''
def OLD_replaceText(text, dictionary):
    res = bytearray()
    while text:
        for k in dictionary:
            if text.startswith(k):
                print(k)
                res += bytes([dictionary[k]])
                text = text[len(k):]
    return res
'''

def tree_to_table(root, prefix, lookup_table):
    element = root[2]

    if type(element) != tuple:
        if prefix == '':
            lookup_table[element] = '0'
        else:
            lookup_table[element] = prefix
    else:
        tree_to_table(element[0], prefix + '0', lookup_table)
        tree_to_table(element[1], prefix + '1', lookup_table)
    return lookup_table


def Huffman_encode(data):
    if data == b'':
        return ''

    table = {}

    # Aggiungo i caratteri alla table, associando ad ogni lettera il numero di occorrenze
    for char in data:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1

    q = PriorityQueue()
    counter_id = 0

    for k,v in table.items():
        q.put((v, counter_id,k))
        counter_id += 1

    while(q.qsize() > 1):
        x = q.get()
        y = q.get()

        sum_freq = (x[0]) + (y[0])
        z = (sum_freq, counter_id,(x,y))
        counter_id += 1
        
        q.put(z)

    root = q.get()

    a = tree_to_table(root, '', {})

    test1 = {k:bitarray(v) for k,v in a.items()}
    test2 = {v: k for k, v in a.items()}

    encoded = bitarray()
    encoded.encode(test1, data)

    return (encoded.to01(), test2)

def Huffman_decode(data, dictionary):
    res = bytearray()
    subs = data[0]
    l = 1
    i = 0
    while data:
        while subs not in dictionary:
            l+=1
            subs = data[:l]

        print(len(res))
        res += bytes([dictionary[subs]])
        print(i)
        i+=1
        data = data[len(subs):]
        if data == '':
            break
        l = 1
        subs = data[0]

    return res


def encodeTable(table):
    tableString = ''
    print(table)

    for k in table:
        tableString += '{0:08b}'.format(len(k)) + k + '{0:08b}'.format(table[k])

    return tableString

def decodeTable():
    
    file = open('dict.huff', 'rb')

    dictionary = {}

    byte = file.read()
    array = bitarray()
    array.frombytes(byte)
    text = array.to01()
    

    while(len(text) >= 8):
        n_bits = int(text[:8], 2)
        text = text[8:]

        key = text[:n_bits]
        text = text[n_bits:]

        value = int(text[:8], 2)
        text = text[8:]

        dictionary[key] = value

    return dictionary


file = open('a.csv', 'rb')
pr = file.read()
(a, table) = Huffman_encode(pr)


compressed_filename = 'test.huff'

output = open(compressed_filename, 'wb')
r = bitarray(a)
t = r.tobytes()
bit_len = r.length()

output.write(bit_len.to_bytes(4, "little"))
output.write(t)
output.close()

output = open(compressed_filename, 'rb')
bit_len_read = int.from_bytes(output.read(4), "little")
print(bit_len_read)

kekw = output.read()
output.close()

a = bitarray()
a.frombytes(kekw)

bits = a.to01()[:bit_len_read]
#print(bits)

#print(table)
x2 = encodeTable(table)
new20 = bitarray(x2)

dict_output = open('dict.huff', 'wb')
dict_output.write(new20.tobytes())
dict_output.close()

print('*' * 100)
decode_table = decodeTable()
print(decode_table)


decoded = Huffman_decode(bits, decode_table)
print(decoded)

decompression_output = open('decompressed_huffman.txt', 'wb')
decompression_output.write(decoded)

