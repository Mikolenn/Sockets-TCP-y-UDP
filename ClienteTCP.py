import socket

# Socket de IPv4 y tipo UDP
sTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Direccion del servidor
serverAddr = ("192.168.0.5", 1024)

sTCP.connect(serverAddr)

continuar = True

while continuar:

    # Mensaje ingresado por el cliente
    dataToSend = raw_input("[Cliente] Ingrese el mensaje a transmitir: ")

    # Se termina la conexion
    if dataToSend.lower() == "fin":

        dataToSend = bytes(dataToSend.encode("utf-8"))
        sTCP.send(dataToSend)
        sTCP.close() 
        continuar = False

    # Se comunica con el servidor
    else:
        # Conversion del string a bytes para su envio
        dataToSend = bytes(dataToSend.encode("utf-8"))

        # Envio del mensaje
        sTCP.send(dataToSend)

        # Respuesta del servidor en bytes
        recievedData = sTCP.recv(1024)

        # Conversion de la respuesta en bytes a String
        recievedData = str(recievedData.decode("utf-8"))

        # Respuesta del servidor en String
        print("\n" + "[Cliente] Mensaje recibido: " + recievedData + "\n")
