import socket

from _thread import *
import threading

msgs=["HI","HI","HI"]
ports=[10001,10002,10003]
def threaded(c):
    while True:

        data = c.recv(1024)

        print("Reciever says: ",data)

        if not data:
            print('Bye')
            break

        c.send(data)

    c.close()


def sender():

    for port in ports:

         host =socket.gethostname()

         s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

         s.connect((host,port))

         print("Connected to port",port)

         message = msgs[port-10001]

         s.send(message.encode('ascii'))
         print("Sending ",message , " to " ,port )
         data=s.recv(1024)

         print('Received from the client :',str(data.decode('ascii')))

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
