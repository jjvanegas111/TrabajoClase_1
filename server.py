import socket

HOST = "10.253.46.136"  # Dirección IP del servidor
PORT = 65432            # Puerto para la comunicación

# Crear el socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Asociar socket con la dirección y puerto
    server_socket.listen()            # Poner el servidor en modo escucha
    print(f"Servidor escuchando en {HOST}:{PORT}")

    client_counter = 0  # Contador de clientes

    while True:
        conn, addr = server_socket.accept()  # Aceptar conexión de un cliente
        client_counter += 1                 # Incrementar el contador de clientes

        with conn:
            print(f"Conectado por {addr} (Cliente {client_counter})")
            while True:
                data = conn.recv(1024)  # Recibir datos del cliente
                if not data:
                    print(f"Conexión cerrada por {addr} (Cliente {client_counter})")
                    break
                print(f"Mensaje recibido de Cliente {client_counter}: {data.decode()}")
                response = f"Echo {client_counter}".encode()  # Crear la respuesta personalizada
                conn.sendall(response)  # Enviar respuesta al cliente
