from chatlib import *
print(build_message("LOGIN","12345678901"))
print(split_data("username#password" , 1))
x=["1","2","3"]
print(join_data(x))
#parse_message(”LOGIN          |    8|user#pass”)")

import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 8820 ))
my_socket.send("Stay calm and keep coding".encode())
data = my_socket.recv(1024).decode()
print("The server sent " + data)
my_socket.close()