import socket

class Sender:

	ip = "127.0.0.1"
	p = 5005
	sock = None

	def __init__(self, ip, p):
		self.ip = ip
		self.p = p
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def send(self, msg):
		self.sock.sendto(msg, (self.ip, self.p))

s = Sender("127.0.0.1", 5005)

#s.send("led-17-O-01")
#s.send("led-17-O-00")
#s.send("led-17-B-31")
s.send("snd")

