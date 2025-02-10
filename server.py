import socket

HOST = "127.0.0.1"  # Dirección IP del servidor (localhost)
PORT = 65432        # Puerto para la comunicación

# Crear el socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Asociar socket con la dirección y puerto
    server_socket.listen()            # Poner el servidor en modo escucha
    print(f"Servidor escuchando en {HOST}:{PORT}")

    conn, addr = server_socket.accept()  # Aceptar conexión de un cliente
    with conn:
        print(f"Conectado por {addr}")
        data = conn.recv(1024)  # Recibir datos del cliente
        if data:
            print(f"Mensaje recibido: {data.decode()}")
            conn.sendall(b"Echo recibido")  # Enviar respuesta al cliente