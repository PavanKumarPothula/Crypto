import socket
import time


ports=[10001,10002,10003]

def getmsg():


     host=socket.gethostname()
     port=10001

     s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.bind((host,port))
     print("socket binded to port",port)

     s.listen(5)
     print("hmm, listening....")

     c,addr=s.accept()

     print("Connected to ",addr[0],':',addr[1])

     msg = c.recv(1024)

     print("Sender says: ",msg.decode('ascii'))

     if not msg:
         print('Bye')

     c.send("Thanks mate".encode('ascii'))

     c.close()

     time.sleep(0)

     shareMyHash(hash(msg))

     s.listen()
     

def shareMyHash(m):

    MCAST_GRP = 224.0.0.1
    MCAST_PORT = 10000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    sock.sendto("Hello World", (MCAST_GRP, MCAST_PORT))

















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
