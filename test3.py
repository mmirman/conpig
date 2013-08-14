import conpiglet

##################
##  TESTING IT  ##
##################

def test(arg):
    for i in range(0,10):
        print arg

conpiglet.spawn(test, "X")    
conpiglet.spawn(test, "O")

conpiglet.waitAll()
