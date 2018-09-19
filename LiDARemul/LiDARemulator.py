import socketserver
from os.path import exists
from time import sleep

HOST = '192.168.0.19'
PORT = 23   #9009
 
class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[%s] Connected' %self.client_address[0])
        filename = "1.bin"
        print('Filename[%s] Transfer Start...' %filename)

        with open(filename, 'rb') as f:
            nNumOfChunk = 0
            data = f.read(1024) 
            f.close()
            
            while True:
                try:
                    self.request.send(data)
                    nNumOfChunk += 1
                    print('%d' %nNumOfChunk)                   
                    sleep(1/100)   # 30Fps
                    
                except KeyboardInterrupt:
                    break
 
        print('File Transfer Done. Num Of chunk[%d] ' %nNumOfChunk)
 
 
def runServer():
    print('++++++File Server Starting++++++')
    print("+++File server Terminated by 'Ctrl + C'.")
 
    try:
        server = socketserver.TCPServer((HOST, PORT),MyTcpHandler)
        server.serve_forever()
    
    except KeyboardInterrupt:
        print('++++++File Server Terminated.++++++')
 
 
runServer()
 
