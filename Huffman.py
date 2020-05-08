from queue import PriorityQueue 

inv_map = {}

def huffman_tree_to_table(root, prefix, lookup_table):
    element = root[2]
    if type(element) != tuple:
        # leaf node
        lookup_table[element] = prefix
    else:
        huffman_tree_to_table(element[0], prefix + "0", lookup_table)
        huffman_tree_to_table(element[1], prefix + "1", lookup_table)
    return lookup_table


def replaceText(dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return res


def HUFFMAN_encode(string):
    table = {}
    # Aggiungo i caratteri alla table, associando ad ogni lettera il numero di occorrenze
    for char in string:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1

    print(table)

    q = PriorityQueue()
    counter_id = 0

    for k,v in table.items():
        q.put((v, counter_id,k))
        counter_id+=1

    #print(list(q.queue))
    #print(q.qsize())

    while(q.qsize() != 1):
        x = q.get()
        y = q.get()

        sum_freq = (x[0]) + (y[0])
        z = (sum_freq, counter_id,(x,y))
        counter_id+=1
        
        q.put(z)

    root = q.get()
    print(root)

    a = huffman_tree_to_table(root, "", {})
    print(a)

    global inv_map
    inv_map = {v: k for k, v in a.items()}

    coded = replaceText(a, string)
    return coded
