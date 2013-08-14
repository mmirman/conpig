import sys

import gevent
import signal

alive = 0

def next(argA, argB):
    signal.setitimer(signal.ITIMER_REAL, 0.00004)
    try:
        gevent.sleep(0)
    except:
        None

def removeOne(g):
    global alive
    alive -= 1

def spawn(method, *args, **kr):
    global alive
    g = gevent.spawn(method, *args, **kr)
    alive += 1
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
    global alive
    while alive > 0:
        # I'm told pause sucks
        try:
            gevent.sleep(0.1)
        except:
            None

##############################
## initialize the scheduler ##
##############################
signal.signal(signal.SIGALRM, next)
next(None,None)
