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


raw_text = 'aaaaaaabcccddefghhiiiiiiiiiiiiiiiiiiiiiiiillmnooop'
'''
raw_text = 'mississippi' * 5000
raw_text = 'mmmmmmssssssiiiii' * 5000
'''
encoded_text = RLE_encode(raw_text)
decoded_text = RLE_decode(encoded_text)

print()
print('*' * 80)
print("Raw text: \t" + raw_text)
print("Encoded text: \t" + encoded_text)
print("Decoded text: \t" + decoded_text)
print('*' * 80)


print(len(raw_text))
print(len(encoded_text))

'''
if raw_text == decoded_text:
    print('\t\t\t\tSUCCESS!\n')
'''