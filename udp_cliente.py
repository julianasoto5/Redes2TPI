import socket

# Configuración del cliente UDP
server_address = ('14.200.8.3', 7)  # Dirección del servidor y puerto UDP echo
message = b'Hola desde el cliente UDP'

# Crear un socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print(f'Enviando: {message}')
    sock.sendto(message, server_address)  # Enviar mensaje

    # Recibir respuesta
    data, server = sock.recvfrom(4096)
    print(f'Recibido: {data}')
