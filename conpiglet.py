import sys

import gevent

import signal
from collections import deque
import time

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

def runMain(main):
    global alive

    signal.signal(signal.SIGALRM, next)
    spawn(main)

    next(None,None)

    while alive > 0:
        # I'm told pause sucks
        gevent.sleep(2)




