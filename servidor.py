import socket
import sqlite3
from datetime import datetime

# Configuración del socket TCP/IP
def inicializar_socket():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(('localhost', 5000))
        servidor.listen()
        print("[Servidor] Escuchando en localhost:5000...")
        return servidor
    except OSError as e:
        print(f"[Error] No se pudo iniciar el servidor: {e}")
        exit()

# Crear base de datos y tabla si no existen
def inicializar_db():
    try:
        conexion = sqlite3.connect('chat.db')
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT,
                fecha_envio TEXT,
                ip_cliente TEXT
            )
        ''')
        conexion.commit()
        conexion.close()
        print("[Servidor] Base de datos lista.")
    except sqlite3.Error as e:
        print(f"[Error] Problema con la base de datos: {e}")
        exit()

# Guardar mensaje recibido en la base de datos
def guardar_en_db(contenido, ip_cliente):
    try:
        conexion = sqlite3.connect('chat.db')
        cursor = conexion.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)', (contenido, fecha, ip_cliente))
        conexion.commit()
        conexion.close()
        print(f"[Servidor] Mensaje guardado: {contenido}")
    except sqlite3.Error as e:
        print(f"[Error] Al guardar mensaje: {e}")

# Aceptar conexiones de clientes
def aceptar_conexiones(servidor):
    while True:
        try:
            cliente_socket, cliente_direccion = servidor.accept()
            print(f"[Servidor] Conexión desde {cliente_direccion}")

            mensaje = cliente_socket.recv(1024).decode()
            print(f"[Servidor] Mensaje recibido: {mensaje}")

            guardar_en_db(mensaje, cliente_direccion[0])

            respuesta = f"Mensaje recibido: {mensaje}"
            cliente_socket.send(respuesta.encode())

            cliente_socket.close()

        except KeyboardInterrupt:
            print("\n[Servidor] Apagando servidor...")
            servidor.close()
            break

# Programa principal
if __name__ == "__main__":
    inicializar_db()
    servidor = inicializar_socket()
    aceptar_conexiones(servidor)
