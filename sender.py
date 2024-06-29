import socket

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
#TARGET_IP= " 192.168.43.179"   jo internet se connect unhe ye likhna h
TARGET_IP = "127.0.0.1"  #localhost
port_no = 2525
target_address = (TARGET_IP, port_no)
quiet = True
while True:
    message = input("Plz enter your message : ")
    message_encrypted = message.encode('ascii')
    s.sendto(message_encrypted,target_address)
    print("Your message has been sent!")
    user_input = input("do you want to quiet it press Y/N : ")
    if user_input == "Y" or user_input =="y":
        quiet = False