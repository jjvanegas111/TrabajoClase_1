import socket
import hashlib

HOST = "10.253.46.136"  # Dirección IP del servidor
PORT = 65432        # Puerto
FILENAME = "aplauso_0.wav"  # Archivo a enviar

# Calcular SHA-256 antes de enviar el archivo
hasher = hashlib.sha256()
with open(FILENAME, "rb") as f:
    while chunk := f.read(4096):
        hasher.update(chunk)

file_hash = hasher.hexdigest()
print(f"SHA-256 del archivo antes de enviarlo: {file_hash}")

# Crear socket del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Enviar el nombre del archivo
    client_socket.sendall(FILENAME.encode())

    # Enviar el archivo al servidor
    with open(FILENAME, "rb") as f:
        while chunk := f.read(4096):
            client_socket.sendall(chunk)

    print("Archivo enviado correctamente.")

    # Recibir SHA-256 del servidor
    server_hash = client_socket.recv(1024).decode()
    print(f"SHA-256 recibido del servidor: {server_hash}")

    # Comparar hashes
    if file_hash == server_hash:
        print("✅ El SHA-256 coincide, el archivo llegó intacto.")
    else:
        print("❌ El SHA-256 NO coincide, el archivo podría estar corrupto.")

'''
for i in {1..5}; do python3 cliente.py & done
'''