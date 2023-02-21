import socket
import hashlib

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                s.listen()
                conn, addr = s.accept()
                continue
            pass_change = data.decode("utf-8")
            salt = "cs361"
            salted_password = pass_change+salt
            hashed_password = hashlib.md5(salted_password.encode())
            send_password = (hashed_password.hexdigest()).encode("utf-8")

            conn.sendall(send_password)
