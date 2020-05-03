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

# Totally broken, MUST FIX!!!
def RLE_decode(string):
    for index, _ in enumerate(string):
        if index % 2 == 0:
            for _ in range(int(string[index])):
                print(string[index+1])

encoded_text = RLE_encode('aaaaaaabcccddefghhiiiiiiiiiiiiiiiiiiiiiiiillmnooop')

print(encoded_text)
#print(RLE_decode(encoded_text))