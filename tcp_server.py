import socket

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto en el que el servidor escuchará
host = '0.0.0.0'  # Acepta conexiones desde cualquier dirección IP
port = 9000

# Asociar el socket con la dirección y el puerto
server_socket.bind((host, port))

# Escuchar por conexiones entrantes
server_socket.listen(5)
print(f"Servidor escuchando en {host}:{port}...")

while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión recibida de {client_address}")

    # Recibir datos del cliente (en este caso no nos importa lo que envíen, los descartamos)
    data = client_socket.recv(1024)  # Recibimos hasta 1024 bytes

    # Aquí simplemente descartamos los datos. No hacemos nada con ellos.
    # Si quisiéramos procesarlos, lo haríamos en este punto.

    # Cerrar la conexión con el cliente
    client_socket.close()
