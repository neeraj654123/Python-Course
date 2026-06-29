import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostname()
port = 12345
s.connect((IP, port))
print("Connected to server!")

while True:
    message_from_server = s.recv(50)
    print("Server: ",message_from_server.decode('utf-8'))
    message_to_send=input("Client: ")
    s.send(bytes(message_to_send,'utf-8'))