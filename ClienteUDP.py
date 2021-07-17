import socket

#socket de IPv4 y UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

continuar = True
while continuar:

    #ingresar caracteres a convertir
    dataOut = raw_input("[Cliente] Ingrese el mensaje a transmitir" + "\n")

    if dataOut != "fin":

        #convertir de string a bytes para enviarlo
        dataOut = bytes(dataOut.encode("utf-8"))

        #enviarlo
        s.sendto(dataOut, ("192.168.0.5", 1024))

        #recibir el mensaje
        dataIn, addr = s.recvfrom(1024)

        #convertirlo de bytes a string
        dataIn = str(dataIn.decode("utf-8"))
        print("\n" + "[Cliente] Mensaje recibido: " + dataIn + "\n")

    #STOP termina la concexion
    else:
        dataOut = bytes(dataOut.encode("utf-8"))
        s.sendto(dataOut, ("192.168.0.5", 1024))
        s.close() 
        continuar = False
