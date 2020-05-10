def longest_match(look_buffer, search_buffer):
    offset_i = offset_j = 0
    length = 0
    max_len = 0
    index = 0

    match = None

    while offset_i < len(search_buffer):
        search_pos = search_buffer[offset_i]
        look_pos = look_buffer[offset_j]

        if search_pos == look_pos:
            length += 1
            offset_j += 1
            offset_i += 1

            if length > max_len:
                max_len = length
                index = offset_i-length
                match = search_buffer[offset_i-length:offset_i]

        else:
            offset_j = 0
            length = 0
            search_pos = search_buffer[offset_i]
            look_pos = look_buffer[offset_j]
            if search_pos == look_pos:
                continue

            offset_i +=1
        
    return (index, match)


def LZ77_encode(data, look_size, search_size):
    current_search_size = 0
    i = 0
    j = 0
    n = 7

    for k in range(n):
        search_buffer = data[i:i+current_search_size]
        look_buffer = data[j:j+look_size]

        match = longest_match(look_buffer, search_buffer)

        if match[1] is None:
            o = 0
            l = 0
            c = look_buffer[0]
        else:
            o = j - match[0]
            l = len(match[1])
            c = data[j + l]

        print('*' * 50 + "Step " + str(k+1) + '*' * 50)
        print("Search buffer: " + search_buffer + "\t(" + str(current_search_size) + ")")
        print("Look-ahead buffer: " + look_buffer + "\t(" + str(look_size) + ")")
        triple = (o, l, c)
        print(triple)
        print(match)

        j += l+1

        #if current_search_size == search_size:


        if current_search_size+l+1 <= search_size:
            current_search_size += (l+1)
        else:
            current_search_size = search_size
 


string = 'abaababaabbaabbbbbbbbb'


LZ77_encode(string, 6, 5)

'''
a = longest_match('cbaba', 'aba')[0]
a = longest_match('ababa', 'aabaabab')
print(a)

#r = dataChar-a[0]
'''