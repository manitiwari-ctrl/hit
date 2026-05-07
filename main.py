import socket
import time

HOST = "0.0.0.0"
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print("Listening on port 3000")

while True:
    conn, addr = s.accept()
    print("Client connected:", addr)
    try:
        while True:
            conn.sendall(b"ping\n")
            time.sleep(1)
    except Exception:
        pass
    finally:
        conn.close()
