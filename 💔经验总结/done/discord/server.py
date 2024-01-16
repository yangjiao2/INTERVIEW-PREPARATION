
import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print (f'client_socket: {client_socket}, client_address: {client_address}')
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        # Get client's name
        client_name = client_socket.recv(1024).decode('utf-8')
        self.clients[client_name] = client_socket

        # Notify everyone about the new client
        self.broadcast(f"{client_name} has joined the chat.")

        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break

                # Check if the message is intended for a specific client
                if message.startswith('@'):
                    recipient_name, msg_content = message.split(' ', 1)
                    recipient_name = recipient_name[1:]
                    if recipient_name in self.clients:
                        recipient_socket = self.clients[recipient_name]
                        recipient_socket.send(f"{client_name}: {msg_content}".encode('utf-8'))
                    else:
                        client_socket.send(f"Error: User '{recipient_name}' not found.".encode('utf-8'))
                else:
                    # Broadcast the message to all clients
                    print ('broadcast')
                    self.broadcast(f"{client_name}: {message}")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Remove the client from the list and close the connection
            del self.clients[client_name]
            client_socket.close()
            self.broadcast(f"{client_name} has left the chat.")

    def broadcast(self, message):
        for client_name, client_socket in self.clients.items():
            try:
                client_socket.send(message.encode('utf-8'))
            except:
                # Remove the client if the connection is broken
                del self.clients[client_name]

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    chat_server = ChatServer(host, port)
    chat_server.start()