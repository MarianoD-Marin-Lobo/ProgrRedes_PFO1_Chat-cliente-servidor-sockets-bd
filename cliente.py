import socket

# Función para enviar mensajes al servidor
def enviar_mensajes():
    while True:
        mensaje = input("Escribe un mensaje (o 'exit' para salir): ")
        if mensaje.lower() == 'exit':
            print("[Cliente] Sesión finalizada.")
            break

        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.connect(('localhost', 5000))

            cliente.send(mensaje.encode())

            respuesta = cliente.recv(1024).decode()
            print(f"[Servidor] {respuesta}")

            cliente.close()
        except ConnectionRefusedError:
            print("[Error] No se pudo conectar al servidor.")
            break

if __name__ == "__main__":
    enviar_mensajes()
