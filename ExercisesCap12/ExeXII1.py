import socket

while True:
        url_name=input('Enter a URL: ')
        try:
            page_web=url_name.split('/')
            host=page_web[2]
            mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock.connect((host, 80))
            cmd = 'GET '+url_name+' HTTP/1.0\r\n\r\n'
            mysock.send(cmd.encode())
        except:
            print('Please enter a valid web address')
            continue  #Debo usar el bucle del inicio o el continue no ejecuta.
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(),end='')
        break
mysock.close()