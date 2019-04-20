import socket
import time
import threading 

ports=[10001,10002,10003]
MyPort=10002
def getmsg():
     global ports
     global MyPort

     host=socket.gethostname()

     s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.bind((host,MyPort))
     print("socket binded to port",MyPort)

     s.listen(5)
     print "hmm, listening...."

     c,addr=s.accept()

     print "Connected to ",addr[0],':',addr[1]

     msg = c.recv(1024)

     print "Sender says: ",msg.decode('ascii')

     if not msg:
         print 'Bye'

     c.send("Thanks mate".encode('ascii'))

     c.close()

     #time.sleep(0)
     try:
     #time.sleep(0)
       #t1=thread.start_new_thread(shareMyHash, (hash(msg),)) 
       #t2=thread.start_new_thread(listenToHashes, ()) 
       t1 = threading.Thread(target=shareMyHash, args=(hash(msg),)) 
       t2 = threading.Thread(target=listenToHashes, args=()) 
     except Exception, e:
        print e
        print "something went wrong"
     
     t1.start()
     t2.start()
     t1.join()
     t2.join()
     return 0

def shareMyHash(msg):
    global ports
    global MyPort


    UDP_IP = "127.0.0.1"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    for p in ports:
         if p != MyPort:
             print "sending my hash ",msg," to port ",p
             sock.sendto(str(msg), (UDP_IP,p))

def listenToHashes():
    global ports
    global MyPort

 
    UDP_IP = "127.0.0.1"
    UDP_PORT = MyPort

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) 
        print "received message:", data





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
