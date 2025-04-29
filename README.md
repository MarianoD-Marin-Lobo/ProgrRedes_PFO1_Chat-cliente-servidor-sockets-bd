# TP - Chat Básico Cliente-Servidor con Sockets y Base de Datos (Python)

### 💡 Objetivo

Este proyecto tiene como fin implementar una aplicación cliente-servidor utilizando sockets TCP en Python, que permita el envío de mensajes desde múltiples clientes al servidor, almacenando cada mensaje en una base de datos SQLite y respondiendo al cliente con una confirmación.

---

### 🧩 Estructura del Proyecto

- `servidor.py`: contiene la lógica del servidor (socket TCP, recepción de mensajes, guardado en la base de datos SQLite).
- `cliente.py`: programa cliente que se conecta al servidor y permite enviar mensajes por consola.
- `chat.db`: base de datos SQLite que almacena los mensajes.
- `README.md`: este archivo con instrucciones del proyecto.

---

### ⚙️ Tecnologías utilizadas

- Python 3.x
- Módulos estándar:
  - `socket`: comunicación entre cliente y servidor.
  - `sqlite3`: para conexión y manejo de la base de datos.
  - `datetime`: para registrar la fecha/hora del mensaje.
- VSCode + SQLite Viewer o DB Browser for SQLite (para ver la base).

---

### 🚀 Cómo ejecutar el proyecto

1. Cloná o descargá este repositorio.
2. Abrí dos terminales en VSCode:
   - En una, corré el servidor:

     ```bash
     python servidor.py
     ```

   - En otra, corré el cliente:

     ```bash
     python cliente.py
     ```

3. En el cliente, escribí mensajes hasta que ingreses `exit` para terminar.
4. Verificá que los mensajes se guarden en `chat.db`.


---

### 🔐 Manejo de errores

- Si el puerto está ocupado, el servidor muestra un mensaje de error.
- Si hay problemas con la base de datos, también se informa en consola.
- Código modularizado y comentado para claridad.

---

### 📚 Desarrollado por...

Alumno: Mariano Daniel Marin
Comisión B
