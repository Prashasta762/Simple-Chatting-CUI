import socket
host='127.0.0.1'
port=9000
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print('Client is Online')
while 1>0:
        message=c.recv(1024)
        if not message:
                break
        print('From Client:'+str(message.decode()))
        message1=input("Enter Message:")
        c.send(message1.encode())
c.close()
