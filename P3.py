import socket
import time
import threading 

ports=[10001,10002,10003]
MyPort=10003
myMsg=""
collectedHashes=[]

def getmsg():
     global ports
     global MyPort
     global myMsg

     host=socket.gethostname()

     s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.bind((host,MyPort))
     print("socket binded to port",MyPort)

     s.listen(5)
     print "hmm, listening...."

     c,addr=s.accept()


     myMsg = c.recv(1024).decode('ascii')

     print "Connected to ",addr[0]," : ",addr[1], "and it says ",myMsg


'''''     s.close()
     time.sleep(2)
     collectedHashes=[]
     for i in ports:
        if i != MyPort:
            collectedHashes.append(listenToHashes())
        else:
            shareMyHash(hash(msg))

'''''
def startThreading():
     global myMsg
     global collectedHashes
     try:
     #time.sleep(0)
       #t1=thread.start_new_thread(shareMyHash, (hash(msg),)) 
       #t2=thread.start_new_thread(listenToHashes, ()) 
       t1 = threading.Thread(target=shareMyHash, args=())
       t2 = threading.Thread(target=listenToHashes, args=()) 
     except Exception,e:
        print "collected before death",collectedHashes
        print e
        print "something went wrong"
     
     t2.start()
     t1.start()
     t1.join()
     t2.join()

     return 0

def shareMyHash():
    global ports
    global MyPort
    global myMsg

    msg=hash(myMsg)

    host =socket.gethostname()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    for port in ports:
        if port != MyPort:

                s.connect((host,port))
                print("Tring to Send ",msg , " to " ,port )
                s.send(str(msg).encode('ascii'))
                print("Sent ",msg , " to " ,port )

    print "Done sharing with em"    

'''''
    UDP_IP = "127.0.0.1"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    for p in ports:
        if p != MyPort:
                print "sending my hash ",msg," to port ",p
                sock.sendto(str(msg), (UDP_IP,p))
'''''

def listenToHashes():
    global ports
    global MyPort
    global collectedHashes
    

    host=socket.gethostname()
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,MyPort))
    s.listen(len(ports))

    c,addr=s.accept()

#    print "Connected to ",addr[0],':',addr[1]

    msg = c.recv(1024).decode('ascii')
    collectedHashes.append(msg)
    
    print "Connected to ",addr[0]," : ",addr[1], "and it says ",msg
    
    c.close()
    print "current list",collectedHashes

''''' 
    UDP_IP = "127.0.0.1"
    UDP_PORT = MyPort

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) 
        print "received message:", data


'''''


'''''    for port in ports:
        if port != 10001:
             host =socket.gethostname()

             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

             s.connect((host,port))

             s.send(m.encode('ascii'))


'''''







'''''


        host =socket.gethostname()

	port = 54321

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	s.connect((host,port))

	message = "Hey Mate"
	while True:

		s.send(message.encode('ascii'))

		data = s.recv(1024)

		print('Received from the server :',str(data.decode('ascii')))

		ans = input('\nDo you want to continue(y/n) :')
		if ans == 'y':
			continue
		else:
			break
	s.close()
'''''
if __name__ == '__main__':
    getmsg()
    startThreading()