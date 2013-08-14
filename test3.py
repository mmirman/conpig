import conpiglet

##################
##  TESTING IT  ##
##################

def test(arg):
    for i in range(0,1000):
        print arg

def main():
    conpiglet.spawn(test, "X")    
    conpiglet.spawn(test, "O")

conpiglet.scheduleMain(main)

