
def longest_match(a, b):
    return (a in b) #Placeholder!!!


def LZ77_encode(data, look_size, search_size):
    current_search_size = 0
    i = 0
    j = 0
    n = 3

    for k in range(n):
        search_buffer = data[i:i+current_search_size]
        look_buffer = data[j:j+look_size]

        if not longest_match(look_buffer, search_buffer):
            o = 0
            l = 0
            c = look_buffer[0]

        print('*' * 50 + "Step " + str(k) + '*' *50)
        print("Search buffer: " + search_buffer + "\t(" + str(current_search_size) + ")")
        print("Look-ahead buffer: " + look_buffer + "\t(" + str(look_size) + ")")
        triple = (o, l, c)
        print(triple)

        j += l+1

        if current_search_size+l+1 <= search_size:
            current_search_size += (l+1)
        else:
            current_search_size = search_size
 



string = 'abaababaabbaabbbbbbbbb'

LZ77_encode(string, 6, 5)