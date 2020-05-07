from queue import PriorityQueue 
import unicodedata

inv_map = {}

def huffman_tree_to_table(root, prefix, lookup_table):
    element = root[2]
    if type(element) != tuple:
        # leaf node
        lookup_table[element] = prefix
    else:
        huffman_tree_to_table(element[0], prefix + "0", lookup_table)
        huffman_tree_to_table(element[1], prefix + "1", lookup_table)
    return lookup_table


def replaceText(dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return res


def HUFFMAN_encode(string):
    table = {}
    # Aggiungo i caratteri alla table, associando ad ogni lettera il numero di occorrenze
    for char in string:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1

    print(table)

    q = PriorityQueue()
    counter_id = 0

    for k,v in table.items():
        q.put((v, counter_id,k))
        counter_id+=1

    print(list(q.queue))
    print(q.qsize())

    while(q.qsize() != 1):
        x = q.get()
        y = q.get()

        sum_freq = (x[0]) + (y[0])
        z = (sum_freq, counter_id,(x,y))
        counter_id+=1
        
        q.put(z)

    root = q.get()
    print(root)
    print("*"*100)

    a = huffman_tree_to_table(root, "", {})
    print(a)

    global inv_map
    inv_map = {v: k for k, v in a.items()}

    #coded = find_replace(string, a)
    coded = replaceText(a, string)
    return coded


string = 'she sells seashells by the seashore' 
#string = 'mississippi' * 5000
#string = 'Hello world'
#string = 'aaabc'
#string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse et libero quam. Pellentesque eros nulla, faucibus vitae lacinia eget, convallis ut nisi. Proin vestibulum justo sed ante rhoncus, ac condimentum ligula finibus. Praesent id finibus velit, in auctor est. Vestibulum iaculis, mi id pharetra dignissim, nibh lacus dapibus ante, nec porta elit arcu in mauris. Ut mollis, tortor vel laoreet consectetur, est magna varius arcu, vitae euismod diam metus vestibulum lectus. Curabitur faucibus scelerisque dolor. Nulla luctus facilisis ex pulvinar placerat. Mauris eget tempor magna.Vivamus a dictum sem. Phasellus a nulla et arcu dictum semper. Praesent massa purus, fermentum ac mollis viverra, aliquet vel nunc. Sed commodo risus felis, et porta nisi sollicitudin in. Pellentesque pulvinar bibendum porta. Nullam nec mattis nulla. Nam luctus scelerisque lobortis. In feugiat tortor sit amet quam tristique porttitor. Ut ac est in nibh scelerisque blandit. Maecenas laoreet, lorem eu porta vehicula, massa sapien sollicitudin sem, et tempus arcu orci vitae justo.Fusce quis leo sit amet nisl facilisis faucibus eget in sem. Morbi nec porttitor nisl. Vestibulum sit amet mi in eros varius fermentum vel sed dui. Sed vel euismod ipsum. Phasellus ac purus viverra, posuere turpis ac, pretium augue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque posuere mi sit amet eros auctor luctus. Vivamus felis odio, auctor non elementum quis, tempus id magna. Vestibulum sit amet tincidunt dui, ac condimentum ex. Aliquam erat volutpat. In sodales, nisl at suscipit posuere, risus sapien sodales orci, imperdiet ultricies nulla nisl at mauris. Integer cursus leo eget tincidunt semper.Nulla purus tortor, sodales quis felis nec, accumsan euismod massa. Cras sodales urna velit, eu sollicitudin ligula aliquet quis. In dapibus massa et odio imperdiet gravida. Nunc a ultrices odio. Nam scelerisque diam sed lectus laoreet placerat. Sed vitae semper metus, id sodales tortor. Phasellus leo ex, rhoncus a ex non, rutrum placerat eros. Ut accumsan orci a ipsum convallis, non ultrices massa gravida. Praesent rutrum consectetur tempus. Integer tempor ultricies sem non varius.Sed tristique nec sem sed iaculis. Aliquam in tempor mi. Pellentesque tempus nisl ac accumsan blandit. Cras luctus nibh eget rhoncus pretium. In auctor, mi efficitur accumsan ultricies, risus est dictum dolor, et pulvinar nunc libero a dui. Ut eu risus quis lectus congue tristique sit amet commodo ipsum. Integer tristique arcu non eros egestas ornare. Nunc pharetra sapien feugiat nunc tempus aliquet. Phasellus congue lacus id leo bibendum vestibulum. Maecenas pharetra molestie justo, ut convallis odio dignissim quis. Sed placerat nunc turpis, in consequat magna posuere nec. Suspendisse eu ex ut enim egestas auctor eget vel orci.Sed nec pharetra lorem. Suspendisse potenti. Nunc at ligula ut nibh interdum efficitur id pharetra turpis. Sed dignissim libero vel laoreet finibus. Donec feugiat ut leo nec gravida. Vivamus quis placerat sem. Etiam viverra urna vel augue facilisis, nec bibendum lacus vehicula. Nullam et pharetra leo. Maecenas sed sapien semper, rutrum ligula sit amet, tincidunt erat. Fusce blandit dapibus mi eu interdum. Morbi accumsan augue vitae neque varius, at elementum elit faucibus. Vestibulum non diam orci. Donec at volutpat arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Fusce vel erat vitae nisi iaculis volutpat at in est.Ut euismod, metus sed feugiat hendrerit, est velit tempus arcu, eget dignissim lectus libero ac nibh. Vivamus ultricies quam in consectetur imperdiet. Etiam vulputate commodo tempus. Aenean vel justo congue, luctus enim eu, rutrum purus. Nam tristique, tellus non congue tempor, diam dui mollis tortor, et semper urna purus a magna. Duis sed est magna. Praesent scelerisque ante metus. Phasellus iaculis dolor sed tellus rhoncus, id auctor metus consectetur.Cras aliquam, odio ut sagittis lacinia, nunc est mattis erat, sed tempus risus massa nec velit. Sed sed commodo ex, id vestibulum felis. Curabitur sagittis nisl ac eros malesuada, a rhoncus elit pellentesque. Fusce imperdiet, ex vel malesuada accumsan, enim sapien maximus diam, vitae semper metus purus ac massa. Nam ac mattis nunc. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam tristique nulla in tortor tempus, sit amet imperdiet neque auctor. Sed sed ipsum felis. Aliquam hendrerit tortor tristique mauris vulputate ultrices. Nullam tempor iaculis orci at tincidunt. Proin mauris metus, posuere non mi vitae, fermentum posuere tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.Vivamus eget turpis sit amet nisi tristique cursus. Nullam id purus eleifend, consectetur diam hendrerit, imperdiet ligula. Praesent tortor velit, volutpat ut velit a, ultrices mattis ex. Nunc consequat aliquam sem, ut finibus arcu euismod et. Suspendisse a leo vitae nunc elementum interdum. Morbi velit dolor, placerat quis nunc nec, mattis viverra mauris. Donec sollicitudin molestie ipsum, in elementum purus. Sed maximus metus at condimentum varius. Phasellus sagittis, nisi sed maximus elementum, dui sem rutrum lorem, eget pellentesque est tellus vitae magna. Mauris at odio ultricies, porttitor dolor id, sodales dolor. Nullam at ornare magna, sit amet fringilla lectus. Sed vitae ultrices felis. Etiam ullamcorper odio quis purus interdum, sed condimentum elit vulputate. Nam iaculis non orci nec mollis. Nam dignissim lacus turpis, non tincidunt ipsum imperdiet in.Donec hendrerit ante vitae mollis tempor. Nulla leo tellus, porttitor quis convallis id, malesuada feugiat sem. Nulla facilisi. Sed quis convallis quam, sed commodo risus. Nulla quis nisl odio. Praesent vel elit id nisl scelerisque fermentum sed a orci. Vivamus vel tellus sit amet nibh dapibus vehicula sed sed eros. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices tellus."

encoded = HUFFMAN_encode(string)
print(string)
print(encoded)

original_bytes = len(string)
compressed_bits = len(encoded)
compressed_bytes = int(compressed_bits/8)

print("Original: " + str(original_bytes) + " byte \tCompressed: " + str(compressed_bytes) + " byte")
print("New file is " + str(int(100 * (compressed_bytes/original_bytes))) + "% lighter")


uncoded = replaceText(inv_map, encoded)
print("REVERSED: " + str(inv_map))
print(uncoded)