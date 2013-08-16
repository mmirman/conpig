Conpig Threading Library
========================

Conpig is a green threading library using green threads from [Gevent](http://www.gevent.org/intro.html)
which are based on [greenlets](https://pypi.python.org/pypi/greenlet).
along side a signal based scheduler.
This allows one true concurrency despite CPython's GIL using green threads instead of OS processes or OS threads such that spawning a new thread is still cheap.

Want
----

* Fast, cheap, easy, traditional concurrency.

Have
----

* Cpython's GIL prevents OS threads from running concurrently and switching context for any reason but to perform IO.

* OS threads are bulky and slow.  Processes are even worse.

* Current green thread implementations require manual context switches.  This is tedious. This is also bug prone for programmers who are used to having a scheduler.

* Processes based libraries like [parallel python](http://www.parallelpython.com/) prevent you from communicating between "threads" with the datastructures you'd usually use.  Again, processes are also slow and buggy.

Solution
--------

* Keep track of green threads in a queue.

* Create a global scheduler using signals to schedule the next context switch.

Drawbacks & Limitations
-----------------------

* A solution to concurrency, not parallelism.

* Conpig threads still can only run on one core of a processor.

Usage
-----

* You can run from a main method

```
import conpig

def test(arg):
    for i in range(0,4000):
        print arg


conpig.spawn(test, "X")    
conpig.spawn(test, "O")

conpig.waitAll()
```

== License

See LICENSE file.