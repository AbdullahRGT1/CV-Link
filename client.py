import socket
import time
import keyboard   # soon as experiment , later switched with openCV output ---> Controller input



client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # preparing the socket


print("ready")



# connection_state = b'0'



pressed_key = '' 

while pressed_key != ('esc'):   # send loop  

    pressed_key = keyboard.read_key()
    print(pressed_key)

    massage = str(pressed_key).encode()

    start_time = time.time()                       # start time 
    client.sendto(massage, ('localhost', 8080))    # send the key name
    data , address = client.recvfrom(1024)         
    latency = (time.time() - start_time) * 1000    # latency 

    #connection_state = data

    print(str(latency)[:5] + "ms")




print("waiting for server...")



data , _ = client.recvfrom(1024) # connected end "not finished"




print(f"the server is off!")





