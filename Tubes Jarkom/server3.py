import socket

#Implementasi pembuatan TCP socket dan mengaitkannya ke alamat dan port tertentu 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inisialisasi Socket TCP/IP
addr = ('', 8080)   #Inisialisasi alamat
serverSocket.bind(addr) #Bind Socket ke alamat tertentu
serverSocket.listen(1) #Listen Koneksi Masuj

while True: #Ketika alamat diterima maka server akan terus berjalan
#Program web server dapat menerima dan memparsing HTTP request yang dikirimkan oleh browser
    print('Server is Running') #Menampilkan string sebagai tanda server sedang berjalan
    connectionSocket, addr = serverSocket.accept() 
    print('Terhubung dengan client:', addr) #Menampilkan string sebagai tanda server sudah terhubung
    
    try:
        
        message = connectionSocket.recv(1024).decode() #Membaca data dari koneksi   
        filename = message.split()[1] # Parse request untuk mendapatkan path file yang diminta
        print(filename) #mencetak file yang diterima
        

#Web server dapat mencari dan mengambil file (dari file system) yang diminta oleh client
        file = open(filename[1:])
        outputdata = file.read()
        file.close()
#Web server dapat membuat HTTP response message yang terdiri dari header dan konten file yang diminta
        header = 'HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: ' + str(len(outputdata)) + '\n\n' #Melakukan inisiasilasi header jika benar
        body = outputdata #Menginisialisasikan body
#Web server dapat mengirimkan response message yang sudah dibuat ke browser (client) dan dapat ditampilkan dengan benar di sisi client
        connectionSocket.send(header.encode()) #Mengirim respons header
        connectionSocket.send(outputdata.encode()) #Mengirim respons body
        
#Jika file yang diminta oleh client tidak tersedia, web server dapat mengirimkan pesan “404 Not Found” dan dapat ditampilkan dengan benar di sisi client.
    except IOError:
        
    
        header = 'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n' #Menginisiliasikan header yang akan ditampilkan jika permintaan tidak benar
        body = '<centre><b>404 not found</b></centre>' #Menginisiliasikan body yang akan ditampilkan jika permintaan tidak benar
        connectionSocket.send(header.encode()) #mengirim respons header
        connectionSocket.send(body.encode()) #Mengirim respons body
     
            
    connectionSocket.close() #Menutup Koneksi
        
serverSocket.close() #Menutup Server

