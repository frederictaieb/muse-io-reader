from liblo import *

import sys 
import time


class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)

    #receive accelrometer data
    @make_method ('/muse/elements/alpha_session_score', 'ffff')
    def alpha_session_score_callback(self, path,args):
        
        alpha_1 = args[0] 
        alpha_2 = args[1]
        alpha_3 = args[2]
        alpha_4 = args[3]

        alpha_avg = (alpha_1 + alpha_2 + alpha_3 + alpha_4)/4

        print "%s:" %(path)
        
        print "1: %f 2:%f 3: %f 4: %f avg: %f" % (
            alpha_1, alpha_2, alpha_3, alpha_4, alpha_avg
        )

        #print "%f" %(alpha_avg)

    @make_method ('/muse/elements/beta_session_score', 'ffff')
    def beta_session_score_callback(self, path,args):
        
        beta_1 = args[0] 
        beta_2 = args[1]
        beta_3 = args[2]
        beta_4 = args[3]

        beta_avg = (beta_1 + beta_2 + beta_3 + beta_4)/4

        print "%s:" %(path)

        print "1: %f 2: %f 3: %f 4: %f avg: %f" % (
            beta_1, beta_2, beta_3, beta_4, beta_avg
        )

        #print "%f" %(beta_avg)

try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()


server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)