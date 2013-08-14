import conpig


##################
##  TESTING IT  ##
##################

def test(arg):
    for i in range(0,20):
        conpig.sleep(1)
        print arg

conpig.spawn(test, "X")    
conpig.spawn(test, "O")

conpig.waitAll()
