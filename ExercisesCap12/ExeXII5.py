import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

response = ''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    response = response + data.decode()
print(response.split('\r\n\r\n')[1]) #si coloco 0 me aparece el encabezado, si coloco 1 me parece el cuerpo del texto, si coloco 2 list index out of range.

mysock.close()
