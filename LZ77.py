'''
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
'''
import random
from ast import literal_eval as make_tuple


def longest_match(data, search_index, look_index, look_size):
    offset_i = search_index
    offset_j = look_index

    length = 0
    max_len = 0
    index = 0
    match = None

    za_warudo = look_index
    flag = False

    #TODO Da pulire e ottimizzare
    while (offset_i < za_warudo or flag) and (offset_j < (look_index+look_size) and offset_j < len(data)):
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

            if offset_i >= za_warudo:
                flag = True

        elif offset_i < za_warudo:
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

verbose = False

def LZ77_encode(data, look_size, search_size):
    current_search_size = 0
    i = 0
    j = 0
    step = 1
    output = ''

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
        #print(triple)

        output += (str(triple) + '\n')

        #step3: ab|aababa|abbaabbbbbbbbb
        #step4: abaa|babaab|baabbbbbbbbb
        #step5: abaab|ab|aabbaa|bbbbbbbbb   #BAD!

        #new5_: ab|aabab|aabbaa|bbbbbbbbb   #ALRIGHT!
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
    output = ''

    for triple in data:
        t = make_tuple(triple)
        o = t[0]
        l = t[1]
        c = t[2]

        i = len(output) - o

        while l > 0:
            output += output[i]
            i += 1
            l -= 1

        output += c

    return output

        


def randomString(length):
    l = ['a', 'b', 'c']

    string = ''
    while length > 0:
        c = random.choice(l)
        seq = c * random.randint(0, 2)
        string += seq
        length -= len(seq)

    return string

#string = 'abaababaabbaabbbbbbbbb'
#string = randomString(random.randint(0, 10))
string = 'ccbbcaccccbbacc' * 3
#string = 'cabracadabrarrarrad'

print(string)

encoded = LZ77_encode(string, 6, 7)

decoded = LZ77_decode(encoded)

print(encoded)

print('*' * 50)
print(decoded)




