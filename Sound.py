import threading
import time
import pygame
from pygame.locals import *

class Sound(threading.Thread):

        def __init__(self):
                threading.Thread.__init__(self)

        def run(self):
                print "Playing Sound"
                pygame.mixer.init()
                pygame.mixer.music.load("myFile.wav")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                        continue
                print "End Playing"