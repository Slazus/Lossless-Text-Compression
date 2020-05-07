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