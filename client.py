import socket
import time
import keyboard   # soon as experiment , later switched with openCV output ---> Controller input



client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # preparing the socket


print("ready")



pressed_key = '' 

while pressed_key != ('esc'):   # a loop  

    pressed_key = keyboard.read_key()
    print(pressed_key)

    massage = str(pressed_key).encode()

    client.sendto(massage, ('localhost', 8080))




print("waiting for server...")



data , _ = client.recvfrom(1024)




print(f"the server is off!")





