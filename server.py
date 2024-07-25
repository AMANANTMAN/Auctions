import socket
import threading

def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            # Decode the data
            decoded_data = data.decode('utf-8')
            print(f"Received: {decoded_data}")
            # You can process the data here or send a response back to the client
            
            client_socket.send(f"Echo: {decoded_data}".encode('utf-8'))
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        client_socket.close()

def start_server(host='127.0.0.1', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
