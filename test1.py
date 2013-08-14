import conpig

##################
##  TESTING IT  ##
##################

def test(arg):
    for i in range(0,4000):
        print arg

conpig.forkIO(test, "X")    
conpig.forkIO(test, "O")
