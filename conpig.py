import gevent
import signal

alive = 0

############################
## the periodic scheduler ##
############################
def next(argA = None, argB = None):
    try:
        if alive > 0:
            signal.setitimer(signal.ITIMER_REAL, 0.00008)
        else:
            signal.setitimer(signal.ITIMER_REAL, 0)

        gevent.sleep(0)
    except:
        pass

##############################
## initialize the scheduler ##
##############################
signal.signal(signal.SIGALRM, next)

#######################
## library functions ##
#######################


def removeOne(g):
    global alive
    alive -= 1

def spawn(method, *args, **kr):
    global alive
    
    g = gevent.spawn(method, *args,**kr)
    alive += 1
    next()
    g.link(removeOne)
    return g

def spawn_after(seconds, function, *args, **kwargs):
    global alive
    g = gevent.spawn_later(seconds, method, *args, **kr)
    alive += 1
    g.link(removeOne)
    return g

def spawn_n(function, *args, **kwargs):
    global alive
    g = gevent.spawn_raw(method, *args, **kr)
    alive += 1
    g.link(removeOne)

sleep = gevent.sleep
getcurrent = gevent.getcurrent

def waitAll():
    """ This is only meant to be run once at the end of the program.  
        It turns off the scheduler when all threads have halted.
        If your program runs on an infinite loop, it needs not be run at all.
    """
    global alive

    try:
        while alive > 0:
            gevent.sleep(1)
    finally: 
        signal.setitimer(signal.ITIMER_REAL, 0)
        
