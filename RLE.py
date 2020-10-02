import time

#Funzione di codifica di RLE
def RLE_encode(data):
    #Inizializzo il contatore di occorrenze
    count = 1

    #Inizializzo la variabile che indica l'ultimo byte letto
    lastByte = data.read(1)

    #Inizializzo l'array di byte
    encoded = bytearray()

    #Loop in cui continuo a leggere un byte alla volta
    while(byte := data.read(1)):
        #Ho raggiunto la fine del file: esco dal loop
        if byte == b'':
            break
        
        #Se il byte appena letto e' uguale al precedente incremento il contatore delle occorrenze
        if byte == lastByte:
            count += 1   
        else:
            #Se e' diverso allora aggiungo il conteggio di occorrenze come primo byte e
            #il simbolo come secondo byte, infine resetto il contatore
            while(count > 255):
                count -= 255
                encoded += bytes([255])
                encoded += lastByte

            encoded += bytes([count])
            encoded += lastByte
            count = 1
        lastByte = byte

    #Aggiungo l'ultima coppia di byte rimanenti e finisco
    while(count > 255):
                count -= 255
                encoded += bytes([255])
                encoded += lastByte

    encoded += bytes([count])
    encoded += lastByte
    return encoded


#Funzione di decodifica di RLE
def RLE_decode(data):
    #Inizializzo l'array di byte
    output = bytearray()
    
    #Loop in cui leggo 2 byte alla volta
    while (byte := data.read(2)):
        #Se ho raggiunto la fine del file termino
        if byte[0] == b'':
            break

        #Aggiungo al mio array il simbolo appena letto dal secondo byte, ripetuto tante volte quante indicate
        #nel valore del primo byte
        #print("Byte: " + str(byte[0]) + " times " + str(byte[1]))
        output += (bytes([byte[1]]) * int(byte[0]))

    return output

