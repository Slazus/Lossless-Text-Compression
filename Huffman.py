from queue import PriorityQueue 

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
    reversed_map = {v: k for k, v in a.items()}

    encoded = replaceText(data, a)
    return (encoded, reversed_map)


def Huffman_decode(data, dict):
    return replaceText(data, dict)

