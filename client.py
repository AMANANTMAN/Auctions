import socket
import time

def send_packets(host='127.0.0.1', port=65432, message='Hello, Server!', interval=1):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    try:
        while True:
            # Send data to the server
            client.sendall(message.encode('utf-8'))
            # Receive response from the server
            response = client.recv(1024)
            print(f"Received from server: {response.decode('utf-8')}")
            # Wait for the specified interval before sending the next packet
            time.sleep(interval)
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    send_packets()
