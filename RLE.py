def RLE_encode(data):
    if data == '':
        return ''

    count = 1
    lastChar = data[0]
    encoded = ''

    for char in data[1 : ]:
        if char == lastChar:
            count = count + 1
        else:
            encoded += (str(count) + lastChar)
            count = 1
        lastChar = char

    encoded += (str(count) + lastChar)
    return encoded


def RLE_decode(data):
    count = ''
    decoded = ''
    for char in data:
        if char.isdigit():
            count += char
        elif char:
            decoded += (char * int(count))
            count = ''
    return decoded