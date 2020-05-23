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
            if(count > 1):
                encoded += (str(count) + lastChar)
                count = 1
            else:
                encoded += lastChar
        lastChar = char

    if(count > 1):
        encoded += (str(count) + lastChar)
    else:
        encoded += lastChar
    return encoded


def RLE_decode(data):
    count = ''
    decoded = ''
    for char in data:
        if char.isdigit():
            count += char
        elif char:
            if count == '':
                decoded += char
            else:
                decoded += (char * int(count))
                count = ''
    return decoded



string = 'aaabbcddefffghhi'

print(string)
encoded = RLE_encode(string)
print(encoded)

print(RLE_decode(encoded))