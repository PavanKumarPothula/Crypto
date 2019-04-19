import socket

def reciever():






     host=socket.gethostname()
     port=10002

     s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.bind((host,port))
     print("socket binded to port",port)

     s.listen(5)
     print("hmm, listening....")

     c,addr=s.accept()

     print("Connected to ",addr[0],':',addr[1])

     data = c.recv(1024)

     print("Sender says: ",data.decode('ascii'))

     if not data:
         print('Bye')
     c.send("Thanks mate".encode('ascii'))

     c.close()




















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
    reciever()
