import socketserver
from os.path import exists
 
HOST = ''    #'192.168.0.26'
PORT = 23   #9009
 
class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[%s] Connected' %self.client_address[0])
        filename = self.request.recv(1024)
        filename = filename.decode()
 
        if not exists(filename):
            return 
 
        print('Filename[%s] Transfer Start...' %filename)
        with opeTn(filename, 'rb') as f:
            try:
                data = f.read(1024) 
                while data: 
                    data_transferred += self.request.send(data)
                    data = f.read(1024)
            except Exception as e:
                print(e)
 
        print('File Transfer Done[%s], Transfer size[%d]' %(filename,data_transferred))
 
 
def runServer():
    print('++++++File Server Starting++++++')
    print("+++File server Terminated by 'Ctrl + C'.")
 
    try:
        server = socketserver.TCPServer((HOST, PORT),MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++File Server Terminated.++++++')
 
 
runServer()
 
