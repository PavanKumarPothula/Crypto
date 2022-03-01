import socket

from _thread import *
import threading

msgs=["HI","HEY","HELLO"]
ports=[10001,10002,10003]

def sender():

    for port in ports:

         host =socket.gethostname()

         s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

         s.connect((host,port))

         print("Connected to port",port)

         message = msgs[port-10001]

         s.send(message.encode('ascii'))
         print("Sending ",message , " to " ,port )
         s.close()



















'''''    host=socket.gethostname()
    port=54321

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    print("socket binded to port",port)

    s.listen(5)
    print("hmm, listening....")

    while True:
        c,addr=s.accept()

        print("Connected to ",addr[0],':',addr[1])

        start_new_thread(threaded, (c,))


    s.close()
'''''
if __name__=='__main__':
    sender()
