def RLE_encode(string):
    count = 1
    lastChar = string[0]
    encoded = ''

    for char in string[1 : : ]:
        if char == lastChar:
            count = count + 1
        else:
            encoded += (str(count) + lastChar)
            count = 1
        lastChar = char

    encoded += (str(count) + lastChar)
    return encoded


def RLE_decode(string):
    count = ''
    decoded = ''
    for char in string:
        if char.isdigit():
            count += char
        elif char:
            decoded += (char * int(count))
            count = ''
    return decoded