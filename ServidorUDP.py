import socket

#socket de IPv4 y UDP
sUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asociar al socket a una direccion y un puerto
sUDP.bind(("192.168.0.5", 1024))

continuar = True
while continuar:

    # Se recibe el mensaje del cliente
    recievedData, clienteAddr = sUDP.recvfrom(1024)

    # Se converte el mensaje de bytes a String
    recievedData = recievedData.decode("utf-8")

    # Finaliza la conexion
    if recievedData.lower() == "fin":

        sUDP.close()
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
        sUDP.sendto(dataToSend, clienteAddr)


