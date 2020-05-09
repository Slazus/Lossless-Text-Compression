'''
while input is not empty do
    prefix := longest prefix of input that begins in window
    
    if prefix exists then
        i := distance to start of prefix
        l := length of prefix
        c := char following prefix in input
    else
        i := 0
        l := 0
        c := first char of input
    end if
    
    output (i, l, c)
    
    s := pop l + 1 chars from front of input
    discard l + 1 chars from front of window
    append s to back of window
repeat
'''

def longest_match(a, b):
    return (a in b)

def LZ77_encode(data, look_size, search_size):
    current_search_size = 0

    i = 0
    j = 0

    n = 2

    for k in range(n):
        search_buffer = data[i:current_search_size]
        look_buffer = data[j:look_size]

        if not longest_match(look_buffer, search_buffer):
            o = 0
            l = 0
            c = look_buffer[0]

        i += l+1
        j += l+1

        if current_search_size+l+1 <= search_size:
            current_search_size += (l+1)
        else:
            current_search_size = search_size

        look_buffer = data[j:look_size+1]    
        search_buffer = data[i:current_search_size+1]

        print('*' * 50 + "Step " + str(k+1) + '*' *50)
        print("Look-ahead buffer: " + look_buffer + "\t(" + str(look_size) + ")")
        print("Search buffer: " + search_buffer + "\t(" + str(current_search_size) + ")")
        triple = (o, l, c)
        print(triple)



string = 'abaababaabbaabbbbbbbbb'
print('*' * 50 + 'Step 0' + '*' * 50)
print(string)

LZ77_encode(string, 6, 5)