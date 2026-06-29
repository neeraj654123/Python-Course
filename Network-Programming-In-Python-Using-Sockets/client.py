import socket
from tkinter import *

def send(list_box,entry):
    message=entry.get()
    list_box.insert(END,'Client: '+message)
    entry.delete(0,END)
    s.send(bytes(message,'utf-8'))

def receive(list_box):
    message = s.recv(50)
    list_box.insert(END,'Server: '+message.decode('utf-8'))

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

root.title('Client')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostname()
port = 12345
s.connect((IP, port))
print("Connected to server!")

root.mainloop()