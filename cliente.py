import socket

HOST = "10.253.46.136"  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor

# Crear el socket del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Conectar al servidor
    client_socket.sendall(b"Echo")       # Enviar mensaje
    data = client_socket.recv(1024)      # Recibir respuesta

print(f"Respuesta del servidor: {data.decode()}")  # Imprimir la respuesta

'''
for i in {1..5}; do python3 cliente.py & done
'''