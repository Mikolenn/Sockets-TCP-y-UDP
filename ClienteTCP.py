import socket

# Socket de IPv4 y tipo TCP
sTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Direccion y puerto del servidor
serverAddr = ("192.168.0.5", 1024)

# Solicitud de conexion con el servidor
sTCP.connect(serverAddr)

continuar = True
while continuar:

    # Impresion del mensaje ingresado por el cliente
    dataToSend = raw_input("\n[Cliente] Ingrese el mensaje a transmitir: ")

    # Verificacion para terminar la conexion
    if dataToSend.lower() == "fin":

        # Conviersion a bytes del mensaje de solicitud para terminar la conexion
        dataToSend = bytes(dataToSend.encode("utf-8"))

        # Envio del mensaje
        sTCP.send(dataToSend)

        # Destruccion del socket
        sTCP.close() 

        continuar = False

    # Comunicacion con el servidor
    else:
        # Conversion del string a bytes para su envio
        dataToSend = bytes(dataToSend.encode("utf-8"))

        # Envio del mensaje
        sTCP.send(dataToSend)

        # Respuesta del servidor en bytes
        recievedData = sTCP.recv(1024)

        # Conversion de la respuesta a String
        recievedData = str(recievedData.decode("utf-8"))

        # Impresion de la respuesta del servidor
        print("\n[Cliente] Respuesta del servidor: " + recievedData)
