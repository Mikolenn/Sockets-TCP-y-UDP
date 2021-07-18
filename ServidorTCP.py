import socket

# Socket de IPv4 y tipo TCP
sTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Direccion y puerto del servidor
serverAddr = ("192.168.0.5", 1024)

# Asociacion del socket a una direccion y un puerto
sTCP.bind(serverAddr)

# Se escuchan solicitudes de enlace con otros sockets
sTCP.listen(1)

# Se acepta la solicitrud de enlace y se captura el socket y su direccion
connection, clienteAddr = sTCP.accept()

# Bienvenida
print("\nConexion con " + str(clienteAddr) + " establecida")

continuar = True
while continuar:

    # Recepcion del mensaje del cliente
    recievedData = connection.recv(1024)

    # Conversion del mensaje de bytes a String
    recievedData = recievedData.decode("utf-8")

    # Verificacion para terminar la conexion
    if recievedData.lower() == "fin":

        # Se destruye el socket del cliente
        connection.close()

        # Se destruye el socket de bienvenida del servidor
        sTCP.close()

        # Mensaje de despedida
        print("\n[Servidor] Conexion con " + str(clienteAddr) + " finalizada\n")

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
        connection.send(dataToSend)


