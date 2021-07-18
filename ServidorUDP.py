import socket

# Socket de IPv4 y tipo UDP
sUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Direccion y puerto del servidor
serverAddr = ("192.168.0.5", 1024)

# Asociacion del socket a una direccion y un puerto
sUDP.bind(serverAddr)

continuar = True
while continuar:

    # Recepcion del mensaje del cliente
    recievedData, clienteAddr = sUDP.recvfrom(1024)

    # Conversion del mensaje de bytes a String
    recievedData = recievedData.decode("utf-8")

    # Verificacion para terminar la conexion
    if recievedData.lower() == "fin":

        # Destruccion el socket del cliente
        sUDP.close()

        # Mensaje de despedida
        print("\n[Servidor] Comunicacion con " + str(clienteAddr) + " finalizada\n")

        continuar = False

    # Respuesta al cliente
    else:
        # Impresion del mensaje recibido
        print("\n[Servidor] Mensaje del cliente: " + recievedData)

        # Conversion del mensaje de minusculas a mayusculas
        dataToSend = recievedData.upper()

        # Conversion de la respuesta a bytes, para su envio
        dataToSend = bytes(dataToSend.encode("utf-8"))

        # Se envia la respuesta
        sUDP.sendto(dataToSend, clienteAddr)


