import socket
import concurrent.futures as pool
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# There must be exactly 16 characters in the key
key = b'Insert Key Here'

cipher = AES.new(key, AES.MODE_ECB)
d_cipher = AES.new(key, AES.MODE_ECB)

def receive_message(conn):
    while True:
        try:
            msg = conn.recv(2048)
            de_msg = unpad(d_cipher.decrypt(msg), AES.block_size)
            f = de_msg.decode('utf-8')
            print(f)
        except:
            print("Server down")
            sys.exit()

HOST_IP = "Insert IP here"
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9191
executor = pool.ThreadPoolExecutor()

name = input("What should be your user name ?\n")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST_IP, PORT))

server.send(name.encode('utf-8'))

executor.submit(receive_message, server)

while True:
    msg = input('')
    msg_w_name = bytes(f'<{name}> {msg}', 'utf-8')
    enc_msg = cipher.encrypt(pad(msg_w_name, AES.block_size))
    server.send(enc_msg)

