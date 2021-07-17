import socket

#socket de IPv4 y UDP
sTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Direccion del servidor
serverAddr = ("192.168.0.5", 1024)

# Asociar al socket a una direccion y un puerto
sTCP.bind(serverAddr)

sTCP.listen(5)

connection, clienteAddr = sTCP.accept()

continuar = True
while continuar:

    # Se recibe el mensaje del cliente
    recievedData = connection.recv(1024)

    # Se converte el mensaje de bytes a String
    recievedData = recievedData.decode("utf-8")

    # Finaliza la conexion
    if recievedData.lower() == "fin":

        connection.close()
        sTCP.close()
        print("\n" + "[Servidor] Conexion con " + str(clienteAddr) + " finalizada")
        continuar = False

    # Se responde al cliente
    else:

        print("\n" + "[Servidor] Mensaje recibido: " + recievedData)

        # Se convierte el mensaje de minusculas a mayusculas
        dataToSend = recievedData.upper()

        #Se converte la respuesta de string a bytes, para su envio
        dataToSend = bytes(dataToSend.encode("utf-8"))

        # Se envia la respuesta
        connection.send(dataToSend)


