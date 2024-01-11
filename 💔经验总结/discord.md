## phone

题目是chat server，build 一个backend service，用socket+multithreading，然后client 用telnet 来测试。
题目分两个部位
第一个部分是最简单的功能，发message，各个client都可以收到。


第二个部分设置用户名字，broadcast msg，提示用户离开之类的，需要存所有的connect，然后遍历发消息。




## Onsite


We wish to create a leader follower distributed system that uses Etcd V2 to coordinate leader election.
The web server will have a single endpoint mounted at /hello, which will do the following:
When the node is considered a leader, it will return "hello world" as its response.
When the node is considered a follower, it will return the port that the leader is running on.


To build this, we will use etcd, which is a distributed, highly available, consistent key value store. For the purposes of this interview however, we will not be running etcd in a highly available configuration.
Use Http Requests/Response for the following V2 APIs (https://etcd.io/docs/v2.3/a̴ ... 5;‍‌pi/)
1. TTL
2. Refresh
3. Compare and Swap




三轮技术面分别是一轮coding，一轮系统，一轮修bug。写代码那轮是要在自己的电脑上下载etcd然后用etcd的api来实现有一个leader和多个follower的一个cluster，一个小时的时间非常紧，因为要读etcd的API，搞清楚要用到的三个API怎么work的，并且还要从零开始写对应的http server，http request/response什么的都要自己处理，我在面试的时候没有提前准备这个，导致面试的一小时内不仅要读API要搞清楚怎么做，还要现场下载etcd。。。系统设计是万年不变的设‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌计多人网游的匹配系统，修bug是面试官给描述系统的各方面，回答你的问题，然后你通过问面试官问题来处理一个prod系统中的事故。



System deisgn 1: design an online gamer matching system. Core requirement: match a user with another user with same (or similar) skill level. lz开始的design比较inefficient，后来经interviewer提示改了一下
3. System design 2 (这一轮应该是specific for MLE): 题目描述很长，但核心requirement就是统计topK + 支持slicing。interviewer表示不要求realtime，所以lz直接用mapreduce design了。interviewer没有challenge太多。


面试官会分享一个json file，内容是每行类似一个log event, 包含用户id, 访问时间，发送信息的对象，要求写一个程序，把log event组成sessions, 有两个要求，一是每个user id自成一个session, 二是每个session最多包含三十分钟窗口内的event（从session的第一个event开始）。还有一些统计信息 比如session有多少event, 发送信息最多的对象等。





----

```py

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

```
---
