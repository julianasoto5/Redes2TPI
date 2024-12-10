import socket

# Dirección IP y puertos del nodo servidor (n9)
servidor = "14.200.12.2"  #dirección IP de n9
puertos = [7, 9]  # Puertos TCP para echo y discard

for puerto in puertos:
    try:
        print(f"Conectando al puerto {puerto}...")
        # Crear socket TCP
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((servidor, puerto))

        # Enviar datos al servidor
        mensaje = f"Prueba desde n13 al servicio en puerto {puerto}\n"
        cliente.sendall(mensaje.encode())

        # Recibir respuesta (solo para echo)
        if puerto == 7:
            respuesta = cliente.recv(1024)
            print(f"Respuesta del servidor: {respuesta.decode()}")
        cliente.close()
    except Exception as e:
        print(f"Error en el puerto {puerto}: {e}")
