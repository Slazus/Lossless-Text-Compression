import random, math
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

            offset_i += 1
        else:
            break
        
    return (index, match)


def getNeededByte(x):
    bitNeeded = math.ceil(math.log2(x+1))

    if bitNeeded <= 8:
        byteLen = 1
    else:
        byteLen = math.ceil(bitNeeded/8)

    return byteLen



def LZ77_encode(data, look_size, search_size):
    current_search_size = 0
    i = 0
    j = 0
    step = 1
    output = bytearray()
    verbose = False

    byteLen = getNeededByte(max(look_size, search_size))

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
        '''
        if verbose:
            print('*' * 50 + "Step #" + str(step) + '*' * 50)
            print("Search buffer: " + search_buffer + "\t(" + str(current_search_size) + ")")
            print("Look-ahead buffer: " + look_buffer + "\t(" + str(look_size) + ")")
            print(match)
        '''
        triple = (o, l, c)
        print(triple)
        print(byteLen)
        output += o.to_bytes(byteLen, 'little')
        output += l.to_bytes(byteLen, 'little')
        output += bytes([c])

        j += l+1

        if (current_search_size+l+1) <= search_size:
            current_search_size += (l+1)
        else:
            current_search_size = search_size

        if j > (search_size-1):
            current_search_size = search_size
            i = j-search_size

        step += 1
    return output



def LZ77_decode(data, number):
    output = bytearray()
    byteLen = getNeededByte(number)

    while (byte := data.read( 2*byteLen + 1)):
        o = byte[0:byteLen]
        l = byte[byteLen:2*byteLen]
        c = byte[2*byteLen:2*byteLen+1]

        if o == b'' or l == b'' or c == b'':
            break

        o = int.from_bytes(o, "little")
        l = int.from_bytes(l, "little")

        i = len(output) - o

        while l > 0:
            output += bytes([output[i]])
            i += 1
            l -= 1

        output += c

    return output


BOKU_GA_KIRA_DA = 2**11
SEARCH_BUFFER_SIZE = BOKU_GA_KIRA_DA - 1
LOOK_BUFFER_SIZE = int(BOKU_GA_KIRA_DA/2)
#SEARCH_BUFFER_SIZE = 255
#LOOK_BUFFER_SIZE = 128

inpt = open('./test/a.pdf', 'rb')

encoded = LZ77_encode(inpt.read(), LOOK_BUFFER_SIZE, SEARCH_BUFFER_SIZE)
inpt.close()
#print(encoded)

compressed_filename = './test/test_w' + str(SEARCH_BUFFER_SIZE) + '.lz77'

outpt = open(compressed_filename, 'wb')
outpt.write(encoded)
outpt.close()

kekw = open(compressed_filename, 'rb')

decompressed = LZ77_decode(kekw, max(LOOK_BUFFER_SIZE, SEARCH_BUFFER_SIZE))
dec_file = open('./test/decoded.pdf', 'wb')
dec_file.write(decompressed)
dec_file.close()

