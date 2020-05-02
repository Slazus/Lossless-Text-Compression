data = "sssabbcccddddeeeeeeff"

def RLE(string):
    count = 1
    lastChar = string[0]
    encoded = ""

    for char in string[1 : : ]:
        if char == lastChar:
            count = count + 1
        else:
            encoded += (str(count) + lastChar)
            count = 1

        lastChar = char

    encoded += (str(count) + lastChar)

    return encoded

rle = RLE(data)
print(rle)