
import socket
import io
 
HOST_Lidar = '192.168.0.19' # Lidar IP
HOST_Android = '192.168.10.2' # Android IP / WiFi APD.. Window Emulator
PORT = 23   #9009
 
def getFileFromServer():

    sockLidar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockLidar.setsockopt(socket.SOL_SOCKET, 25, str("eth0" + '\0').encode('utf-8'))
    sockLidar.connect((HOST_Lidar,PORT))
    
    sockAndroid = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockAndroid.setsockopt(socket.SOL_SOCKET, 25, str("wlan0" + '\0').encode('utf-8'))
    sockAndroid.connect((HOST_Android,PORT))

    nNumOfRecv = 0
    nNumOfForward = 0
    tempBuffer = io.BytesIO()

    while True:
        try:
            tempBuffer = sockLidar.recv(1024)
            nNumOfRecv += 1
            
            sockAndroid.send(tempBuffer)
            nNumOfForward += 1
            
            print('[%d] [%d]', nNumOfRecv, nNumOfForward)
        except KeyboardInterrupt:
            break
            
    print( '####### End  HAHAHA  #########.' )
        

getFileFromServer()