import conpig


##################
##  TESTING IT  ##
##################

def test(arg):
    for i in range(0,4000):
        print arg

def main():
    conpig.forkIO(test, "X")    
    conpig.forkIO(test, "O")

conpig.runMain(main)
