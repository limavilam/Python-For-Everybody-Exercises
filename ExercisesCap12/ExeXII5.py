import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
#Si imprimo cmd me va salir bytes

data = mysock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4   # Finds the end of header
print(message[header_end_pos:])




