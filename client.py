import socket

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# send a message to the server
client_socket.sendall(b"Hello Server!")

input("Press Enter to disconnect...")
client_socket.close()
