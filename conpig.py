#   Copyright 2013 Matthew Mirman
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import gevent
import signal

alive = 0

############################
## the periodic scheduler ##
############################
def next(argA = None, argB = None):
    try:
        if alive > 0:
            signal.setitimer(signal.ITIMER_REAL, 0.0005)
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

def spawn_after(seconds, method, *args, **kwargs):
    global alive
    g = gevent.spawn_later(seconds, method, *args, **kr)
    alive += 1
    g.link(removeOne)
    return g

def spawn_n(method, *args, **kwargs):
    global alive
    g = gevent.spawn_raw(method, *args, **kr)
    alive += 1
    g.link(removeOne)

sleep = gevent.sleep
getcurrent = gevent.getcurrent

def wait_all():
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
        
