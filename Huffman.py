from queue import PriorityQueue 
from bitarray import bitarray

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


def replaceText(text, dictionary):
    res = ''
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return res


def Huffman_encode(data):
    if data == '':
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
    #encoded = replaceText(data, a)
    return (encoded.to01(), test2)


def Huffman_decode(data, dict):
    return replaceText(data, dict)


file = open('test.txt', 'rb')
pr = file.read()
(a, table) = Huffman_encode(pr.decode("utf-8") )
print(pr.decode("utf-8") )
print(table)
print(a)

output = open('test.rle', 'wb')
r = bitarray(a)
t = r.tobytes()
bit_len = r.length()

output.write(bit_len.to_bytes(4, "little"))
output.write(t)

output = open('test.rle', 'rb')
bit_len_read = int.from_bytes(output.read(4), "little")
print(bit_len_read)

kekw = output.read()

a = bitarray()
a.frombytes(kekw)

bits = a.to01()[:bit_len_read]
print(bits)

decoded = Huffman_decode(bits, table)
print(decoded)
