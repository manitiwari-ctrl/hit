import socket
import time
import threading
import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 3000))

def handle_client(conn, addr):
    print("Client connected:", addr)
    try:
        while True:
            conn.sendall(b"ping\n")
            time.sleep(1)
    except Exception as e:
        print("Client disconnected:", addr, e)
    finally:
        conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)

print(f"Streaming server listening on {HOST}:{PORT}")

while True:
    conn, addr = s.accept()
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
