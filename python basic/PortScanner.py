import socket

for port in range(0,11):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect(("google.ocm",port))
		print("PORT",port,".........IS OPEN!!")
		s.close()
	except:
		print("PORT",port,"Close")