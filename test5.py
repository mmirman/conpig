import conpig

##################
##  TESTING IT  ##
##################

def test1(arg):
    for i in range(0,5):
        conpig.sleep(1)
        print arg
    raise Hello    

def test2(arg):
    for i in range(0,10):
        conpig.sleep(1)
        print arg
        

conpig.spawn(test1, "X")    
conpig.spawn(test2, "H")    
test2("O")


conpig.waitAll()
