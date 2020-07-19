def RLE_encode(file):
    count = 1

    lastChar = file.read(1)
    #lastChar = data[0]
    encoded = bytearray()

    while(True):
        byte = file.read(1)
        if byte == b'':
            break
        print(byte)
        if byte == lastChar:
            count += 1 
        else:
            encoded += bytes([count])
            encoded += lastChar
            count = 1
        lastChar = byte

    encoded += bytes([count])
    encoded += lastChar
    return encoded


def RLE_decode(data):
    output = bytearray()

    while (byte := data.read(2)):
        if byte[0] == b'':
            break

        output += (bytes([byte[1]]) * byte[0])

    return output



file = open('test.txt', 'rb')
a = RLE_encode(file)

output = open('test.rle', 'wb')
output.write(a)

output = open('test.rle', 'rb')

decoded = RLE_decode(output)
dec_file = open('decoded.txt', 'wb')
dec_file.write(decoded)