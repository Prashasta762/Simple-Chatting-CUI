import socket
host='127.0.0.1'
port=9000
s=socket.socket()
s.connect((host,port))
print('Host is Online')
print("type 'exit'to stop chatting")
string=input("Enter Message:")
while string.lower()!='exit':
	s.send(str.encode())
	message=s.recv(1024)
	message=message.decode()
	print("From Server:"+message)
	string=input("Enter Message:")
s.close()
