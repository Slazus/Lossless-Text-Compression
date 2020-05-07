from queue import PriorityQueue 

def huffman_tree_to_table(root, prefix, lookup_table):
    element = root[2]
    if type(element) != tuple:
        # leaf node
        lookup_table[element] = prefix
    else:
        huffman_tree_to_table(element[0], prefix + "0", lookup_table)
        huffman_tree_to_table(element[1], prefix + "1", lookup_table)
    return lookup_table


def find_replace(string, dictionary):
    # is the item in the dict?
    for item in string:
        # iterate by keys
        if item in dictionary.keys():
            # look up and replace
            string = string.replace(item, dictionary[item])
    # return updated string
    return string


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

    print(list(q.queue))
    print(q.qsize())

    while(q.qsize() != 1):
        x = q.get()
        y = q.get()

        sum_freq = (x[0]) + (y[0])
        z = (sum_freq, counter_id,(x,y))
        counter_id+=1
        
        q.put(z)

    root = q.get()
    print(root)
    print("*"*100)

    a = huffman_tree_to_table(root, "", {})
    print(a)

    coded = find_replace(string, a)
    return coded

string = 'she sells seashells by the seashore' 
#string = 'mississippi'
#string = 'Hello world'
#string = 'aaabc'

encoded = HUFFMAN_encode(string)
print(string)
print(encoded)
print(len(encoded))