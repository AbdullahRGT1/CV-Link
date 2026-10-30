import socket
import keyboard




def get_ip():

    temp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # preparing a temp socket to get the IP

    # taking network ip by making Google request
    try:
        temp_s.connect(("8.8.8.8", 80))  # server ip
        ip = temp_s.getsockname()[0]
    except:
        ip = "127.0.0.1"  # local mode
    finally:
        temp_s.close()

    return ip




ip = get_ip()

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # preparing a temp socket to record the IP

server.bind((ip, 8080))

print(f"Server is listening on {ip}:8080")





keys = {
    "bus": "up",
    "airplane": "right",
    "boat": "down",
    "car": "left",
}


current_key = None
data = ''.encode()
address = ("",0)

while data.decode() != "close-class"  :              # receive loop

    data , address = server.recvfrom(1024)
    massage = data.decode()
    if massage != ("None" or "close-class") :
        print(keys[str(massage)])

    #Keyboard section
    new_key = keys.get(massage)

    if new_key != current_key:
        if current_key is not None:
            keyboard.release(current_key)

        if new_key is not None:
            keyboard.press(new_key)

        current_key = new_key


    server.sendto(b'1', address)

    #print(f"request from {address} \n {massage}")



if current_key is not None:
    keyboard.release(current_key)


server.sendto('esc'.encode(), address)
server.close()
print(f"the server is off!")
