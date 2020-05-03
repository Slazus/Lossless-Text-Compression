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
            #print(char * int(count), end='')
            decoded += (char * int(count))
            count = ''
    return decoded


raw_text = 'aaaaaaabcccddefghhiiiiiiiiiiiiiiiiiiiiiiiillmnooop'

encoded_text = RLE_encode(raw_text)
decoded_text = RLE_decode(encoded_text)

print()
print('*' * 80)
print("Raw text: \t" + raw_text)
print("Encoded text: \t" + encoded_text)
print("Decoded text: \t" + decoded_text)
print('*' * 80)

if raw_text == decoded_text:
    print('\t\t\t\tSUCCESS!\n')
