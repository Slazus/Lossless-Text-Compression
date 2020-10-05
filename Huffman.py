from queue import PriorityQueue 
from bitarray import bitarray


#Funzione che si occupa di codificare la tabella in una stringa
def encodeTable(table):
    tableString = ''
    #Per ogni chiave nella tabella formatto a dovere la stringa:
    #la lunghezza del prefix code espressa in 8 bit, il prefix code e altri
    #8 bit per il byte associato al prefix code 
    for k in table:
        tableString += '{0:08b}'.format(len(k)) + k + '{0:08b}'.format(table[k])
    return tableString


#Funzione che decodifica la tabella
def decodeTable():
    #Apro il file contenente la tabella
    file = open('./test/table.huff', 'rb')

    #Inizializzo alcune variabili e leggo la tabella trasformandone il
    #contenuto in una stringa binaria
    dictionary = {}
    byte = file.read()
    file.close()
    array = bitarray()
    array.frombytes(byte)
    text = array.to01()
    
    #Fino a quando ho dei byte da leggere
    while(len(text) >= 8):
        #Parsing del numero di bit da leggere
        n_bits = int(text[:8], 2)
        
        #Parsing di chiavi e valori del dizionario
        text = text[8:]
        key = text[:n_bits]
        text = text[n_bits:]
        value = int(text[:8], 2)
        text = text[8:]
        dictionary[key] = value
    return dictionary


#Funzione che converte la rappresentazione "ad albero" in una tabella 
def treeToTable(root, prefix, lookup_table):
    element = root[2]
    #Se l'elemento attuale non rappresenta una ennupla
    if type(element) != tuple:
        #Se il prefisso e' vuoto lo imposto a zero 
        if prefix == '':
            lookup_table[element] = '0'
        #Altrimenti lo imposto direttamente
        else:
            lookup_table[element] = prefix
    #Se abbiamo una ennupla chiamo ricorsivamente la funzione, una volta
    #aggiungendo '0' al prefix e una volta '1', in questo modo tale da
    #"srotolare" tutto l'albero
    else:
        treeToTable(element[0], prefix + '0', lookup_table)
        treeToTable(element[1], prefix + '1', lookup_table)
    return lookup_table


#Funzione che codifica il contenuto del file
def encodeBody(data):
    if data == b'':
        return ''

    table = {}

    # Aggiungo i caratteri alla table, associando ad ogni lettera il numero di occorrenze
    for char in data:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1

    #Creo una coda e un contatore che funge da identificatore
    q = PriorityQueue()
    counter_id = 0

    #Per ogni chiave-valore della tabella inserisco la coppia
    #nella coda
    for k,v in table.items():
        q.put((v, counter_id,k))
        counter_id += 1

    #Fino a quando la coda non e' vuota ottengo due nodi, creo
    #il terzo nodo dato dalla somma delle frequenze dei due e
    #aggiungo quest'ultimo alla coda
    while(q.qsize() > 1):
        x = q.get()
        y = q.get()

        sum_freq = (x[0]) + (y[0])
        z = (sum_freq, counter_id,(x,y))
        counter_id += 1
        
        q.put(z)

    #Estraggo l'ultimo nodo
    root = q.get()

    #Converto l'albero in una tabella
    a = treeToTable(root, '', {})

    #Effettuo la codifica del contenuto e preparo la tabella in un certo
    #formato
    t = {k:bitarray(v) for k,v in a.items()}
    table2 = {v: k for k, v in a.items()}
    encoded = bitarray()
    encoded.encode(t, data)
    return (encoded.to01(), table2)


#Effettua la decodifica del contenuto
def decodeBody(data, dictionary):
    #Inizializzo e imposto i valori
    res = bytearray()
    subs = data[0]
    l = 1

    #Finché ci sonod dati da leggere cerco iterativamente dei prefix
    #code che siano presenti nella tabella
    while data:
        while subs not in dictionary:
            l += 1
            subs = data[:l]
            
        #Aggiungo il valore associato al prefix code attraverso la
        #tabella
        res += bytes([dictionary[subs]])
        
        #Scorro il buffer dei dati
        data = data[len(subs):]

        #Se non ci sono piu' dati concludo
        if data == '':
            break

        #Ritorno alle impostazioni iniziali per la prossima iterazione
        l = 1
        subs = data[0]
    return res




#Funzione della codifica di Huffman
def Huffman_encode(file):
    #Leggo il contenuto del file
    data = file.read()
    file.close()

    #Codifico il contenuto del file e preparo la tabella
    (a, table) = encodeBody(data)
    output = bytearray()

    #Formatto l'output del body a dovere: 4 byte per il numero di bit da leggere
    #e X byte contenenti il corpo codificato
    bodyBits = bitarray(a)
    bodyBytes = bodyBits.tobytes()
    bitsLen = bodyBits.length()
    output += bitsLen.to_bytes(4, "little")
    output += bodyBytes

    #Codifico anche la tabella e vado ad esportarla nel file 'table.huff'
    encodedTable = encodeTable(table)
    tableBits = bitarray(encodedTable)
    tableBytes = tableBits.tobytes()
    dictOutput = open('./test/table.huff', 'wb')
    dictOutput.write(tableBytes)
    dictOutput.close()
    return output


#Funzione di decodifica di Huffman
def Huffman_decode(file):
    #Decodifico la tabella
    decodedTable = decodeTable()
    
    #Parsing del numero di bit da leggere
    bitLen = int.from_bytes(file.read(4), "little")    
    
    #Leggo il contenuto del file e procedo con la decodifica del corpo
    data = file.read()
    file.close()
    bits = bitarray()
    bits.frombytes(data)
    bitString = bits.to01()[:bitLen]
    res = decodeBody(bitString, decodedTable)
    return res
