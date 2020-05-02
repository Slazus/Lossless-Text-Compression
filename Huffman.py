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

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()