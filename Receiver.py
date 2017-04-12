import socket
from Led import *
from Sound import *


class Receiver(threading.Thread):
  ip = "127.0.0.1"
  p = 5005
  sock = None

  def __init__(self, ip, p):
    threading.Thread.__init__(self)
    self.ip = ip
    self.p = p
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock.bind((ip, p))

  def run(self):
    while True:
      data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
      print "%s received by : %s" %(data, str(addr))
  
      #Led
      if data[0:3] == "led":
        gpio = data[4:6]
        cmd = data[7]
        param = data[9:11]
        l = Led(gpio, cmd, param)
        l.start()
      else:
        s = Sound()
        s.start()

r = Receiver("192.168.77.3", 5005)
r.start()