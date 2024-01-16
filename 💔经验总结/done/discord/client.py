import socket
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.host, self.port))

        # Get and send the client's name to the server
        client_name = input("Enter your name: ")
        self.client_socket.send(client_name.encode('utf-8'))

        # Start a thread to handle receiving messages
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        # Main loop to send messages to the server
        try:
            while True:
                message = input()
                self.client_socket.send(message.encode('utf-8'))
        except KeyboardInterrupt:
            print("KeyboardInterrupt: Exiting the chat.")
            self.client_socket.close()

    def receive_messages(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode('utf-8')
                print(message)
        except Exception as e:
            print(f"Error: {e}")
            self.client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    chat_client = ChatClient(host, port)
    chat_client.start()
