import socket
from threading import Thread

PORT = 3001

class Server:

    def __init__(self, port= PORT):
        self.port = PORT
        self.host = 'localhost'
        self.clients = []
        # self.server_socket = None

    def start(self):
        # open up a port for listening to clients
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
        server_socket.bind((self.host, self.port))  # bind host address and port together
        print (server_socket)
        server_socket.listen()
            
        def listen(client):
            try:
                while True:
                        
                    # display client msg
                    # print ('client: ', client)
                    msg = client.recv(1024).decode() # utf
                    # print ('msg: ', msg)

                    # send to clients
                    for c in self.clients:
                        if c != client:
                            c.send(msg.encode())
                
            except:
                self.clients.remove(client)
                for c in self.clients:
                    c.send('someone leaving'.encode())
                print (len(self.clients))


        while True:
            client, address = server_socket.accept()
            self.clients.append(client)
            t = Thread(target = listen, args = [client] )
            t.start()



server = Server()
server.start()