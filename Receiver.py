import socket
from Led import *
from Sound import *

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
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

  '''
  if data[0:3] == "led":
    l = Led(int(data[3:5]))
    if data[6:7] == "1":
      l.led_on()
    elif data[6:7] == "0":
      l.led_off()
    elif data[6:7] == "3":
      l.led_blink(int(data[7:8]), float(data[8:9]))
    else:
      print "Unknown Command"
  elif data[0:3] == "snd":
    print "Son Recu"
  else:
    print "Unknown Command"
  '''