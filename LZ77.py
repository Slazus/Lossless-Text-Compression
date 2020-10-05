import math

#Funzione che restituisce il match più lungo e vicino alla fine del
#search buffer
def longestMatch(data, search_index, look_index, look_size):
    #Imposto gli offset iniziali dei due buffer
    offset_i = search_index
    offset_j = look_index

    #Inizializzo le mie variabili
    length = 0
    max_len = 0
    index = 0
    match = None
    flag = False


    #Loop che si arresta una volta soddisfatte le condizioni di ricerca
    while (offset_i < look_index or flag) and (offset_j < (look_index+look_size) and offset_j < len(data)):
        search_pos = data[offset_i]
        look_pos = data[offset_j]

        #Se la posizione del search buffer corrisponde a quella del look buffer
        #incremento gli offset e la dilatazione della finestra
        if search_pos == look_pos:
            length += 1
            offset_j += 1
            offset_i += 1

            #Se la lunghezza massima della finestra e' stata raggiunta
            #memorizzo le informazioni raccolte nelle rispettive variabili
            if length >= max_len:
                max_len = length
                index = offset_i-length
                match = data[offset_i-length:offset_i]

            #Setto un flag nel caso in cui l'offset i superi la posizione del
            #look buffer
            if offset_i >= look_index:
                flag = True

        #Se la posizione del search buffer non corrisponde e l'offset i e'
        #minore dell'indice del look buffer, allora continuo con la ricerca
        #del longest match
        elif offset_i < look_index:
            offset_j = look_index
            length = 0
            search_pos = data[offset_i]
            look_pos = data[offset_j]

            #Se ho una corrispondenza tra search e look buffer vado
            #alla successiva iterazione senza incrementare l'offset i
            if search_pos == look_pos:
                continue

            offset_i += 1

        #Se l'offset e' maggiore o uguale all'indice del look buffer ho
        #finito e posso concludere la ricerca
        else:
            break
    return (index, match)


#Funzione che ritorna il numero di byte minimo per rappresentare il valore x
def getNeededBytes(x):
    bitNeeded = math.ceil(math.log2(x))
    return math.ceil(bitNeeded/8)


#Funzione di codifica LZ77, che prende come argomento una windowSize
def LZ77_encode(file, windowSize):
    data = file.read()

    #Inizializzo e imposto le variabili 
    current_search_size = 0
    search_max_index = math.ceil(windowSize/2)
    look_max_index = search_max_index
    i = 0
    j = 0
    output = bytearray()

    #Ottengo il numero di byte necessari a rappresentare il
    #massimo numero richiesto per offset e length
    byteLenO = getNeededBytes(search_max_index+1)
    byteLenL = getNeededBytes(windowSize)

    #Itero finché l'indice j non ha raggiunto la fine dei dati
    while j < len(data):
        #Aggiorno la dilatazione del look buffer
        look_buffer = data[j:j+look_max_index]

        #Cerco il nuovo longest match 
        match = longestMatch(data, i, j, look_max_index)

        #Se non ho trovato nessun match, ricado nel caso base dell'algoritmo
        if match[1] is None:
            o = 0
            l = 0
            c = look_buffer[0]
        #Altrimenti devo calcolare opportunamente i parametri <offset, length e
        #next byte (c)>
        else:
            o = j - match[0]
            sentry = len(match[1])
            if j+sentry >= len(data):
                extra = len(data) - j
                l = extra-1
                c = data[len(data)-1]
            else:
                l = len(match[1])
                c = data[j + l]

        
        #Inserisco la tripla di valori in byte
        output += o.to_bytes(byteLenO, 'little')
        output += l.to_bytes(byteLenL, 'little')
        output += bytes([c])

        #Incremento l'indice j in funzione di quanto letto
        j += l+1

        #Eseguo varie operazioni per aggiustare a dovere
        #la dimensione della finestra rispettando eventuali
        #limiti
        if (current_search_size+l+1) <= search_max_index:
            current_search_size += (l+1)
        else:
            current_search_size = search_max_index

        if j > (search_max_index-1):
            current_search_size = search_max_index
            i = j-search_max_index
    return output


#Funzione di decodifica LZ77, prende anche lei come argomento una windowSize
def LZ77_decode(data, windowSize):
    output = bytearray()

    #Calcolo i byte necessari in maniera speculare a quanto fatto prima
    byteLenO = getNeededBytes(math.ceil(windowSize/2)+1)
    byteLenL = getNeededBytes(windowSize)

    #Leggo, in relazione al numero di byte richiesti, la tripla di valori
    #<offset, length, c>
    while (byte := data.read(byteLenO+byteLenL+1)):
        o = byte[0:byteLenO]
        l = byte[byteLenO:byteLenO+byteLenL]
        c = byte[byteLenO+byteLenL:byteLenO+byteLenL+1]

        #Se per qualche motivo (come la fine del file) trovo uno dei valori
        #nulli, allora posso concludere la fase di decodifica
        if o == b'' or l == b'' or c == b'':
            break

        o = int.from_bytes(o, "little")
        l = int.from_bytes(l, "little")

        i = len(output) - o

        #Fino a quando ho dei byte da elaborare trasferisco i byte decodificati
        #come output
        while l > 0:
            output += bytes([output[i]])
            i += 1
            l -= 1

        output += c
    return output