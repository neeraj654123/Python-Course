import socket

from tkinter import *

def send(list_box,entry):
    message=entry.get()
    list_box.insert(END,'Server: '+message)
    entry.delete(0,END)
    client.send(bytes(message,'utf-8'))

def receive(list_box):
    message_from_client = client.recv(50)
    list_box.insert(END,'Client: '+message_from_client.decode('utf-8'))

root =Tk()
entry =Entry(root)
entry.pack(side=BOTTOM)

list_box=Listbox(root)
list_box.pack()

send_btn=Button(root,text='Send',command=lambda:send(list_box,entry))
send_btn.pack()

receive_btn=Button(root,text='Receive',command=lambda:receive(list_box))
receive_btn.pack()

root.minsize(400, 300)
root.maxsize(800, 600)

root.title('Server')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostname()
port = 12345

s.bind((IP, port))
s.listen(4)

print("Server is waiting for connections...")

client, address = s.accept()

  
root.mainloop()