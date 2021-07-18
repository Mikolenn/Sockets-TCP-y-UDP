import socket

# Socket de IPv4 y tipo UDP
sUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Direccion y puerto del servidor
serverAddr = ("192.168.0.5", 1024)

continuar = True

while continuar:

    # Impresion del mensaje ingresado por el cliente
    dataToSend = raw_input("\n[Cliente] Ingrese el mensaje a transmitir: ")

    # Verificacion para terminar la comunicacion
    if dataToSend.lower() == "fin":

        # Conviersion a bytes del mensaje de solicitud para terminar la comunicacion
        dataToSend = bytes(dataToSend.encode("utf-8"))

        # Envio del mensaje
        sUDP.sendto(dataToSend, serverAddr)

        # Destruccion del socket
        sUDP.close() 

        continuar = False

    # Comunicacion con el servidor
    else:
        # Conversion del string a bytes para su envio
        dataToSend = bytes(dataToSend.encode("utf-8"))

        # Envio del mensaje
        sUDP.sendto(dataToSend, serverAddr)

        # Respuesta del servidor en bytes
        recievedData, auxAddr = sUDP.recvfrom(1024)

        # Conversion de la respuesta a String
        recievedData = str(recievedData.decode("utf-8"))

        # Impresion de la respuesta del servidor
        print("\n[Cliente] Respuesta del servidor: " + recievedData)
