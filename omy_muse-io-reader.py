from liblo import *

import sys 
import time


class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)
        alpha_score = 0.0
        beta_score = 0.0
        relaxed_score = 0.0

    def compute_alpha_score(self, a1, a2, a3, a4):
        self.alpha_score = (a1+a2+a3+a4)/4

    def compute_beta_score(self, b1, b2, b3, b4):
        self.beta_score = (b1+b2+b3+b4)/4

    def compute_relaxed_factor(self):
        self.relaxed_score = (self.alpha_score + self.beta_score)/2


    def isRelaxed (self):
        print "relaxed"

    #receive accelrometer data
    @make_method ('/muse/elements/alpha_session_score', 'ffff')
    def alpha_session_score_callback(self, path,args):
        
        a1 = args[0] 
        a2 = args[1]
        a3 = args[2]
        a4 = args[3]

        self.compute_alpha_score(a1, a2, a3, a4)
        print "%s: %f (%f %f %f %f)" %(path, self.alpha_score, a1, a2, a3, a4)

    @make_method ('/muse/elements/beta_session_score', 'ffff')
    def beta_session_score_callback(self, path,args):

        b1 = args[0] 
        b2 = args[1]
        b3 = args[2]
        b4 = args[3]

        self.compute_beta_score(b1, b2, b3, b4)
        print "%s: %f (%f %f %f %f)" %(path, self.beta_score, b1, b2, b3, b4)
 
try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()


server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)