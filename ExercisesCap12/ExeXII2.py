import socket

while True:
        url_name=input('Enter a URL: ')
        try:
            page_web=url_name.split('/')
            host=page_web[2]
            mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock.connect((host, 80))
            count = 0
            cmd = 'GET '+url_name+' HTTP/1.0\r\n\r\n'
            mysock.send(cmd.encode())
        except:
            print('Please enter a valid web address')
            continue  #Debo usar el bucle del inicio o el continue no ejecuta.
        while True:
            data = mysock.recv(512)
            if len(data) < 1 or count >= 3000:
                break
            count = count + len(data)
            print(data.decode(),end='')
            print("The total data is:" ,count)
        break
mysock.close()