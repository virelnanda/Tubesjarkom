# python 3
from socket import *
#Implementasi pembuatan TCP socket dan mengaitkannya ke alamat dan port tertentu 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 12000))
serverSocket.listen(1)
while True:
    print("Server is running")
    connectionSocket, addr = serverSocket.accept()
    try:
#Program web server dapat menerima dan memparsing HTTP request yang dikirimkan oleh browser
        message = connectionSocket.recv(1024)
        filename = message.split()[1].decode('utf-8').strip("/")
        print(filename)
#Web server dapat mencari dan mengambil file (dari file system) yang diminta oleh clien
        f = open(filename)
        outputdata = f.read()
        f.close()
#Web server dapat membuat HTTP response message yang terdiri dari header dan konten file yang diminta
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
        for i in range(0, len(outputdata)):
#Web server dapat mengirimkan response message yang sudah dibuat ke browser (client) dan dapat ditampilkan dengan benar di sisi client
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
#Jika file yang diminta oleh client tidak tersedia, web server dapat mengirimkan pesan “404 Not Found” dan dapat ditampilkan dengan benar di sisi client.
        connectionSocket.send('404 Not Found'.encode())
        connectionSocket.close()
serverSocket.close()