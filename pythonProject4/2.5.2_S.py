import socket
import time
import random
NAME="doron"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8823))
server_socket.listen()
print("Server is up and running")
(client_socket, client_address) = server_socket.accept()
print("Client connected")
data = ""
while True:
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)
    if data=="NAME":
        client_socket.send(NAME.encode())
    elif data=="TIME":
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        client_socket.send(current_time.encode())
    elif data=="RAND":
        r=str(random.randint(1,10))
        print (r)
        client_socket.send(r.encode())

    elif data == "Bye":
        data = " "
    elif data == "Quit":
        print("closing client socket now...")
        client_socket.send("Bye".encode())
        break
    elif data == "":
        client_socket.send("please enter somthing".encode())
    else:
        client_socket.send("not valid data".encode())


client_socket.close()
server_socket.close()