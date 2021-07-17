import socket

# Socket de IPv4 y tipo UDP
sUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
serverAddr = ("192.168.0.5", 1024)

continuar = True

while continuar:

    # Mensaje ingresado por el cliente
    dataToSend = raw_input("[Cliente] Ingrese el mensaje a transmitir: ")

    # Se termina la conexion
    if dataToSend.lower() == "fin":

        dataToSend = bytes(dataToSend.encode("utf-8"))
        sUDP.sendto(dataToSend, serverAddr)
        sUDP.close() 
        continuar = False

    # Se comunica con el servidor
    else:
        # Conversion del string a bytes para su envio
        dataToSend = bytes(dataToSend.encode("utf-8"))

        # Envio del mensaje
        sUDP.sendto(dataToSend, serverAddr)

        # Respuesta del servidor en bytes
        recievedData, auxAddr = sUDP.recvfrom(1024)

        # Conversion de la respuesta en bytes a String
        recievedData = str(recievedData.decode("utf-8"))

        # Respuesta del servidor en String
        print("\n" + "[Cliente] Mensaje recibido: " + recievedData + "\n")
