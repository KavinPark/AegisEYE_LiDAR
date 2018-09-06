import socket

 
HOST = '192.168.0.26' #'localhost'
PORT = 23   #9009
 
def getFileFromServer():
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        nNumOfChunk = 0
        
        while True:
            try:
                sock.recv(1024)
                nNumOfChunk += 1
                print('[%d] ' %nNumOfChunk )
                continue
            except KeyboardInterrupt:
                break
            
        print( 'File Transfer Done. Num Of check[%d]', nNumOfChunk )
        

getFileFromServer()