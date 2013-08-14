import conpig


##################
##  TESTING IT  ##
##################

def test(arg):
    for i in range(0,1000):
        print arg

conpig.spawn(test, "X")

test("O")

