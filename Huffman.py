from Node import *
import math

def printBinary(x):
    print("{0:b}".format(x))


table = {}
table2 = {}
#string = 'she sells seashells by the seashore'

#This is an example because this doesn't work!!!
string = 'mississippi'

# Aggiungo i caratteri alla table, associando ad ogni lettera il numero di occorrenze
for char in string:
    if char in table:
        table[char] += 1
    else:
        table[char] = 1

print(table)

sorted_table = {k: v for k, v in sorted(table.items(), key = lambda item: item[1])}

N = len(sorted_table)
print(sorted_table)

bits = int(math.log2(N)) + 1 #TOFIX

b = '0' * bits
print(b)

a = int(b,2)
for k, v in sorted_table.items():
    table2[k] = "{0:b}".format(a)
    a += int('1' ,2)

print(table2)