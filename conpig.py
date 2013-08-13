import sys

from greenlet import greenlet
import signal
import os
from multiprocessing import Process
from collections import deque
import time

threads = deque([])

def next(argA, argB):
    global threads
    
    if len(threads) == 0: 
        return

    t = threads.popleft()
    
    if t.dead:
        return next(argA,argB)

    threads.append(t)
    t.switch()

def forkIO(method, *args, **kr):
    def methodp():
        method(*args,**kr)
    threads.append(greenlet(methodp))

def runMain(main):
    def mainProcess():
        forkIO(main)
        signal.signal(signal.SIGCHLD, next)
        # attempt to reap every 4 seconds
        while len(threads) > 0:
            time.sleep(4) 

    process = Process(target = mainProcess)
    
    try: 
        process.start()
        pid = process.pid
    
        while process.is_alive():
            time.sleep(0.000001)
            os.kill(pid, signal.SIGCHLD)
            
    finally:
        process.terminate()


def test(arg):
    for i in range(0,4000):
        print arg



def main():
    forkIO(test, "X")    
    forkIO(test, "O")

runMain(main)



    
