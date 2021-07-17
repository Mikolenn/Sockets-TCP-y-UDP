import socket

#socket de IPv4 y UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#asociar socket
s.bind(("192.168.0.5", 1024))

continuar = True
while continuar:

    #recibir el mensaje
    dataIn, addr = s.recvfrom(1024)

    #convertirlo de bytes a string
    dataIn = dataIn.decode("utf-8")

    if dataIn != str("fin"):
        print("\n" + "[Servidor] Mensaje recibido: " + dataIn)

        #de minusculas a mayusculas
        dataOut = dataIn.upper()

        #convertir de string a bytes para enviarlo
        dataOut = bytes(dataOut.encode("utf-8"))

        #enviarlo
        s.sendto(dataOut, addr)

    #STOP termina la concexion
    else:
        s.close()
        print("\n" + "[Servidor] Conexion finalizada " + str(addr))
        continuar = False
