
import socket
 
HOST = '192.168.10.2'   # RPi WiFi APD
PORT = 23   #9009
 
def runAndroid():
 
    sockAndroid = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockAndroid.bind((HOST, PORT))
    sockAndroid.listen(0)
    sockLidar, addr = sockAndroid.accept()

    nNumOfChunk = 0
        
    while True:
        try:
            sockLidar.recv(1024)
            nNumOfChunk += 1
            print('[%d] ' %nNumOfChunk )
            continue
        
        except KeyboardInterrupt:
            break
            
    print( 'File Transfer Done. Num Of check[%d]', nNumOfChunk )
        

runAndroid()

