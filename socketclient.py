#Socket client in Python by Federico De Faveri

import socket


DEST = ('127.0.0.1', 80)

print ("Creating Socket...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("Connecting to ", DEST[0] , " at port " , DEST[1])

s.connect(DEST)

print("Connected!")

print("sending GET request...")



s.sendall(b'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n')

print ("request sent, now reading reply from server...\n")
reply = s.recv(4096)

print (reply)


print("Closing Connection...")
s.close()
