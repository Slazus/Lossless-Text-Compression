import random, math


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
    bitNeeded = math.ceil(math.log2(x))
    byteNeeded = math.ceil(bitNeeded/8)

    return byteNeeded


'''
def LZ77_encode(data, look_size, search_size):
    current_search_size = 0
    i = 0
    j = 0
    step = 1
    output = bytearray()

    byteLen = getNeededByte(max(look_size, search_size))

    while j < len(data):
        #search_buffer = data[i:i+current_search_size]
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
        
            print('*' * 50 + "Step #" + str(step) + '*' * 50)
            print("Search buffer: " + search_buffer + "\t(" + str(current_search_size) + ")")
            print("Look-ahead buffer: " + look_buffer + "\t(" + str(look_size) + ")")
            print(match)
        
        
        #triple = (o, l, c)
        #bakemono += (l+1) 
        #print("BAKEMONO " + str(bakemono))
        #print(triple)
        #print(byteLen)
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
'''


def LZ77_encode(data, windowSize):
    current_search_size = 0
    search_max_index = math.ceil(windowSize/2)
    look_max_index = search_max_index
    i = 0
    j = 0
    step = 1
    output = bytearray()

    byteLen = getNeededByte(search_max_index)

    while j < len(data):
        look_buffer = data[j:j+look_max_index]

        match = longest_match(data, i, j, look_max_index)

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

        output += o.to_bytes(byteLen, 'little')
        output += l.to_bytes(byteLen*2, 'little')
        output += bytes([c])

        j += l+1

        if (current_search_size+l+1) <= search_max_index:
            current_search_size += (l+1)
        else:
            current_search_size = search_max_index

        if j > (search_max_index-1):
            current_search_size = search_max_index
            i = j-search_max_index

        step += 1

    return output



def LZ77_decode(data, windowSize):
    output = bytearray()
    byteLen = getNeededByte(math.ceil(windowSize/2))

    while (byte := data.read( 3*byteLen + 1)):
        o = byte[0:byteLen]
        l = byte[byteLen:3*byteLen]
        c = byte[3*byteLen:3*byteLen+1]

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



'''
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
'''

'''
WINDOW_SIZE = 256

inpt = open('./test/board.bmp', 'rb')

encoded = LZ77_encode(inpt.read(), WINDOW_SIZE)
inpt.close()
#print(encoded)

compressed_filename = './test/testB_w' + str(WINDOW_SIZE) + '.lz77'

outpt = open(compressed_filename, 'wb')
outpt.write(encoded)
outpt.close()

print("Compression DONE")

kekw = open(compressed_filename, 'rb')

#TODO
decompressed = LZ77_decode(kekw, WINDOW_SIZE)
dec_file = open('./test/decodedB.bmp', 'wb')
dec_file.write(decompressed)
dec_file.close()
'''