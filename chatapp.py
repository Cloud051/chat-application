import socket
import threading

# server config
HOST = "127.0.0.1"
PORT = 12345

# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

def handle_client(client_socket, addr):
    print(f"Client {addr} connected.")
    
    # keep receiving data until the client disconnects
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            print(f"Received from {addr}: {data.decode('utf-8')}")
        
        # send a simple confirmation back
            client_socket.sendall(b"Message received!")
        
    except (ConnectionResetError, ConnectionAbortedError):
        print(f"Client {addr} lost connection unexpectedly.")
    
    # clean up when finished
    finally:
        client_socket.close()
        print(f"Client {addr} disconnected.")

def main():
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        client_socket, addr = server_socket.accept() # accepts new connections
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, addr) # creates a new thread for each client
        )
        client_handler.start()

if __name__ == "__main__":
    main()
