table = {}
string = 'she sells seashells by the seashore'

# Aggiungo i caratteri alla table, associando ad ogni lettera il numero di occorrenze
for char in string:
    if char in table:
        table[char] += 1
    else:
        table[char] = 1

print(table)

print({k: v for k, v in sorted(table.items(), key=lambda item: item[1])})