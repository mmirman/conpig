Conpig Threading Library
========================

Conpig is a green threading library using green threads from [Gevent](http://www.gevent.org/intro.html)
which are based on [greenlets](https://pypi.python.org/pypi/greenlet).
along side a signal based scheduler.
This allows one true concurrency using green threads instead of OS processes or OS threads such that spawning a new thread is still cheap.

Want
----

* Fast, cheap, easy, traditional concurrency.

Have
----

* Cpython's GIL prevents OS threads from running concurrently and switching context for any reason but to perform IO.

* OS threads are bulky and slow.  Processes are even worse.

* Current green thread implementations require manual context switches. This is tedious. This is also bug prone for programmers who are used to having a scheduler.

* Processes based libraries like [parallel python](http://www.parallelpython.com/) prevent you from communicating between "threads" with the datastructures you'd usually use.  Again, processes are also slow and buggy.

Solution
--------

* Create a global scheduler using signals to schedule the next context switch.

Drawbacks & Limitations
-----------------------

* A solution to concurrency, not parallelism.

* Conpig threads still can only run on one core of a processor.

* Context switches still only occur every [CPython tick](http://www.dabeaz.com/python/UnderstandingGIL.pdf).

* You still need cooperative yields if you want true fairness for programs that don't do as much IO.

Installing (pip to come)
------------------------

* Need: [Greenlet](https://pypi.python.org/pypi/greenlet)  & [Gevent](http://www.gevent.org/intro.html).

1. Install [Greenlet](https://pypi.python.org/pypi/greenlet) with pip.

2. Install [Gevent](http://www.gevent.org/intro.html) 
    - The old version depends on libevent.  The new github version depends on libev
    - On OSX the install path for libevent is wrong even if you use Mac Ports. 
    - The easiest install method is to [download v.1 from github](https://github.com/surfly/gevent), and install from source using the provided "setup.py".  

Usage
-----

* You can run from a main method

```python
import conpig

def test(arg):
    for i in range(0,4000):
        print arg


conpig.spawn(test, "X")    
conpig.spawn(test, "O")

conpig.wait_all()
```

Authors
-------

* Matthew Mirman

* Eric Faust

License
-------

See LICENSE file.
