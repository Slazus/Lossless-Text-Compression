from queue import PriorityQueue 
from bitarray import bitarray
import time

def treeToTable(root, prefix, lookup_table):
    element = root[2]

    if type(element) != tuple:
        if prefix == '':
            lookup_table[element] = '0'
        else:
            lookup_table[element] = prefix
    else:
        treeToTable(element[0], prefix + '0', lookup_table)
        treeToTable(element[1], prefix + '1', lookup_table)
    return lookup_table


def encodeBody(data):
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

    a = treeToTable(root, '', {})

    test1 = {k:bitarray(v) for k,v in a.items()}
    test2 = {v: k for k, v in a.items()}

    encoded = bitarray()
    encoded.encode(test1, data)

    return (encoded.to01(), test2)



def encodeTable(table):
    tableString = ''

    for k in table:
        tableString += '{0:08b}'.format(len(k)) + k + '{0:08b}'.format(table[k])

    return tableString



def decodeTable():
    file = open('./test/table.huff', 'rb')

    dictionary = {}

    byte = file.read()
    file.close()
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


def Huffman_encode(file):
    data = file.read()
    file.close()
    (a, table) = encodeBody(data)
    output = bytearray()

    bodyBits = bitarray(a)
    bodyBytes = bodyBits.tobytes()
    bitsLen = bodyBits.length()
    output += bitsLen.to_bytes(4, "little")
    output += bodyBytes

    encodedTable = encodeTable(table)
    tableBits = bitarray(encodedTable)
    tableBytes = tableBits.tobytes()

    dictOutput = open('./test/table.huff', 'wb')
    dictOutput.write(tableBytes)
    dictOutput.close()

    return output


def decodeBody(data, dictionary):
    res = bytearray()
    subs = data[0]
    l = 1
    
    while data:
        while subs not in dictionary:
            l += 1
            subs = data[:l]
            
        res += bytes([dictionary[subs]])
        
        data = data[len(subs):]
        if data == '':
            break
        l = 1
        subs = data[0]

    return res


def Huffman_decode(file):
    decodedTable = decodeTable()
    
    bitLen = int.from_bytes(file.read(4), "little")    
    
    data = file.read()
    file.close()
    bits = bitarray()
    bits.frombytes(data)
    bitString = bits.to01()[:bitLen]

    do = decodeBody(bitString, decodedTable)
    
    return do
