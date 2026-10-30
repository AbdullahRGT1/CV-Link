import socket
import time
import opencv_render

# import keyboard



client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # preparing the socket

print('staring in 10s')
time.sleep(5)
print("ready")






while True:   # send loop

    render = opencv_render.render_loop()

    if render == 3:
        print("ended")

        break

    massage = str(opencv_render.cls).encode()

    start_time = time.time()                       # start time 
    client.sendto(massage, ('192.168.1.2', 8080))    # send the className button name


    data, address = client.recvfrom(1024)
    latency = (time.time() - start_time) * 1000    # latency
    print(str(latency)[:5] + "ms")





print("waiting for server...")


client.sendto(b"close-class", ("192.168.1.2", 8080))
data , _ = client.recvfrom(1024) # connected end "not finished"




print(f"the server is off!")





