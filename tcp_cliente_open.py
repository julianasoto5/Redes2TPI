import socket

import argparse

#Configurar el parser de argumentos
parser = argparse.ArgumentParser(description="Se debe indicar IP origen")
parser.add_argument("servidor", type=str, help="Dirección IP del servidor de origen")
args = parser.parse_args();
source_servidor = args.servidor;
# Dirección IP y puertos del nodo servidor (n9)
servidor = "14.200.12.2"  # Dirección IP de n9
puertos = [7, 9]  # Puertos TCP para echo y discard

# Crear y conectar al puerto 7 (echo)
puerto = puertos[0]
print(f"Conectando al puerto {puerto}...")
# Crear socket TCP
cliente_7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_7.connect((servidor, puerto))

# Enviar datos al servidor en puerto 7
mensaje_7 = f"Prueba desde {source_servidor} al servicio en puerto {puerto}\n"
cliente_7.sendall(mensaje_7.encode())

# Recibir respuesta (solo para echo)
respuesta_7 = cliente_7.recv(1024)
print(f"Respuesta del servidor en puerto {puerto}: {respuesta_7.decode()}")

# Crear y conectar al puerto 9 (discard)
puerto = puertos[1]
print(f"Conectando al puerto {puerto}...")
cliente_9 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_9.connect((servidor, puerto))

# Enviar datos al servidor en puerto 9
mensaje_9 = f"Prueba al servidor {servidor} en puerto {puerto}\n"
cliente_9.sendall(mensaje_9.encode())

# Mantener ambas conexiones abiertas hasta que el usuario decida cerrarlas
input("Conexiones abiertas. Presione Enter para cerrar las conexiones...")

# Cerrar las conexiones
cliente_7.close()
cliente_9.close()
