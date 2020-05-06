from Node import *
from queue import PriorityQueue 


def huffman_tree_to_table(root, prefix, lookup_table):
    """Converts the Huffman tree rooted at "root" to a lookup table"""
    if type(root[1]) != tuple:
        # leaf node
        lookup_table[root[1]] = prefix
    else:
        huffman_tree_to_table(root[1][0], prefix + "0", lookup_table) #recursion
        huffman_tree_to_table(root[1][1], prefix + "1", lookup_table) #recursion
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
    print()

    q = PriorityQueue()

    for k,v in table.items():
        q.put((v,k))

    print(list(q.queue))
    print(q.qsize())


    while(q.qsize() != 1):
        x = q.get()
        y = q.get()

        print(str(x) + "\t" + str(y))

        sum_freq = x[0] + y[0]
        z = Node(sum_freq, sum_freq)
        z.right = Node(x, x[0])
        z.left = Node(y, y[0])
        q.put((sum_freq, (x,y)))

    root = q.get()

    a = huffman_tree_to_table(root, "", {})
    print(a)

    coded = find_replace(string, a)
    return coded

#string = 'she sells seashells by the seashore'   #NOT WORKING...
string = 'mississippi'  #WORKING!

print(string)
print(HUFFMAN_encode(string))


