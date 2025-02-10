import socket
import hashlib

HOST = "10.253.46.136"  # Dirección IP del servidor
PORT = 65432            # Puerto para la comunicación

# Crear el socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Asociar socket con la dirección y puerto
    server_socket.listen()            # Poner el servidor en modo escucha
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()  # Aceptar conexión de un cliente
        
        with conn:
            print(f"Conectado con {addr}")

            # Recibir el nombre del archivo
            filename = conn.recv(1024).decode()
            print(f"Recibiendo archivo: {filename}")

            # Establecer un timeout para detectar fin de transmisión
            conn.settimeout(2)  # 2 segundos de espera sin recibir datos

            # Recibir archivo
            with open(f"recibido_{filename}", "wb") as f:
                try:
                    while True:
                        data = conn.recv(4096)
                        if not data:
                            break
                        f.write(data)
                except socket.timeout:
                    print("Timeout alcanzado. Se asume que el archivo se ha recibido completamente.")

            print("Archivo recibido correctamente.")

            # Calcular SHA-256 del archivo recibido
            hasher = hashlib.sha256()
            with open(f"recibido_{filename}", "rb") as f:
                while chunk := f.read(4096):
                    hasher.update(chunk)

            file_hash = hasher.hexdigest()
            print(f"SHA-256 del archivo recibido: {file_hash}")

            # Enviar SHA-256 al cliente
            conn.sendall(file_hash.encode())
            print("Hash enviado al cliente.")
