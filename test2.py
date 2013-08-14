import conpig


##################
##  TESTING IT  ##
##################

def test(arg,ti):
    for i in range(0,20):
        conpig.sleep(ti)
        print arg

conpig.spawn(test, "X", 1)    
conpig.spawn(test, "O", 2)

conpig.waitAll()
