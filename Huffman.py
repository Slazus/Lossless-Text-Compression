from Node import *

table = {}
string = 'she sells seashells by the seashore'

# Aggiungo i caratteri alla table, associando ad ogni lettera il numero di occorrenze
for char in string:
    if char in table:
        table[char] += 1
    else:
        table[char] = 1

print(table)

sorted_table = {k: v for k, v in sorted(table.items(), key = lambda item: item[1])}
print(sorted_table)

'''
a = Node(1, 4)
b = Node(2, 5)
c = Node(3, 6)

a.addParent(c) # left(C) = A     (1)
b.addParent(c) # right(C) = B    (2)

c.PrintTree()
'''

nodes = []
N = len(sorted_table)
print(sorted_table)
for k,v in sorted_table.items():
    print(k, end='')
    nodes.append(Node(k, v))

print(nodes[1].data)