import os

with open('random.txt', 'wb') as fout:
    fout.write(os.urandom(2**32)) # replace 1024 with size_kb if not unreasonably large