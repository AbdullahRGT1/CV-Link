import socket
import time




server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # preparing the socket

server.bind(("localhost", 8080)) # server ip 

print("Server is listening on 127.0.0.1:8080")




data = ''.encode()
address = ("",0)

while (data.decode() != "esc")  :              # receive loop 

    data , address = server.recvfrom(1024)
    server.sendto(b'1', address)
    
    print(f"request from {address} \n {data.decode()}")



server.sendto('esc'.encode(), address)


print(f"the server is off!")




