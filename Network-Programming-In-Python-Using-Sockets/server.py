import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostname()
port = 12345
s.bind((IP, port))
s.listen(4)
print("Server is waiting for connections...")
client,address = s.accept()

while True:
    message = input("Server: ")
    client.send(bytes(message,'utf-8'))
    message_from_client=client.recv(50)
    print("Client: ",message_from_client.decode('utf-8'))
 