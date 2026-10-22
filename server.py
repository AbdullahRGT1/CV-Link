import socket
import keyboard
import time




server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # preparing the socket

server.bind(("192.168.1.16", 8080)) # server ip

print("Server is listening on 192.168.1.16:8080")




data = ''.encode()
address = ("",0)

while (data.decode() != "esc")  :              # receive loop 

    data , address = server.recvfrom(1024)
    massage = data.decode()

    keyboard.press_and_release(massage)       # keyboard click by the name of keys in the massage

    server.sendto(b'1', address)

    print(f"request from {address} \n {massage}")






server.sendto('esc'.encode(), address)


print(f"the server is off!")




