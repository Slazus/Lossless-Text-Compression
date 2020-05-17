import random
from ast import literal_eval as make_tuple


def longest_match(data, search_index, look_index, look_size):
    offset_i = search_index
    offset_j = look_index

    length = 0
    max_len = 0
    index = 0
    match = None
    flag = False

    while (offset_i < look_index or flag) and (offset_j < (look_index+look_size) and offset_j < len(data)):
        search_pos = data[offset_i]
        look_pos = data[offset_j]

        if search_pos == look_pos:
            length += 1
            offset_j += 1
            offset_i += 1

            if length >= max_len:
                max_len = length
                index = offset_i-length
                match = data[offset_i-length:offset_i]

            if offset_i >= look_index:
                flag = True

        elif offset_i < look_index:
            offset_j = look_index
            length = 0
            search_pos = data[offset_i]
            look_pos = data[offset_j]
            if search_pos == look_pos:
                continue

            offset_i +=1
        else:
            break
        
    return (index, match)



def LZ77_encode(data, look_size, search_size):
    current_search_size = 0
    i = 0
    j = 0
    step = 1
    output = ''
    verbose = False

    while j < len(data):
        search_buffer = data[i:i+current_search_size]
        #if j+look_size >= len(data):
        look_buffer = data[j:j+look_size]

        match = longest_match(data, i, j, look_size)

        if match[1] is None:
            o = 0
            l = 0
            c = look_buffer[0]
        else:
            o = j - match[0]
            sentry = len(match[1])
            if j+sentry >= len(data):
                extra = len(data) - j
                l = extra-1
                c = data[len(data)-1]
            else:
                l = len(match[1])
                c = data[j + l]

        if verbose:
            print('*' * 50 + "Step #" + str(step) + '*' * 50)
            print("Search buffer: " + search_buffer + "\t(" + str(current_search_size) + ")")
            print("Look-ahead buffer: " + look_buffer + "\t(" + str(look_size) + ")")
            print(match)

        triple = (o, l, c)
        output += (str(triple) + '\n')

        j += l+1

        if current_search_size+l+1 <= search_size:
            current_search_size += (l+1)
        else:
            current_search_size = search_size

        if j > search_size-1:
            current_search_size = search_size
            i = j-search_size

        step+=1
    return output


def LZ77_decode(data):
    data = data.splitlines()
    output = bytearray()

    for triple in data:
        t = make_tuple(triple)
        o = t[0]
        l = t[1]
        c = int(t[2])

        i = len(output) - o

        while l > 0:
            output.append(output[i])
            i += 1
            l -= 1

        output.append(c)

    return output
