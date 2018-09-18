import socket

 
HOST = '192.168.0.19' #'localhost'
PORT = 23   #9009
 
def getFileFromServer(filename):
    data_transferred = 0
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, 25, str("eth0" + '\0').encode('utf-8'))
        sock.connect((HOST,PORT))
        sock.sendall(filename.encode())
 
        data = sock.recv(1024)
        if not data:
            print('File[%s]: There\'s No File on Server or Transmission Error' %filename)
            return
 
        with open(filename, 'wb') as f:
            try:
                while  data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)
 
    print('File[%s] Transfer Done. Size [%d]' %(filename, data_transferred))
 
filename = '1.bin'  #input('Enter Filename of Saved:')
getFileFromServer(filename)