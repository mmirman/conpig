import conpig


##################
##  TESTING IT  ##
##################

def test(arg):
    for i in range(0,4000):
        print arg


conpig.spawn(test, "X")    
conpig.spawn(test, "O")

conpig.waitAll()
