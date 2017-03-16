# Basical comparison between async and sync function

Async operation will really speed up your code for blocking I/O operations or networks requests.
But it requires to work carefully with even loop and code might be more complicated

## Synchronous/Blocking IO: Sequential Execution

In synchronous operations everything is simple, you have a code that working step by step
On each operation your resources are blocked till that operation will not return control to the program

img[src="https://docs.hhvm.com/s/0dd2cca2312e80ce/images/async/async-sequential.png"]

## Asynchronous Execution

All Python code executes in the main request thread, but main advantage of asynchronous operation is that 
I/O does not block it, and multiple I/O or other async tasks can execute concurrently. 
Usually 90% of the time program spends on I/O, database, network operations.

img[src="https://docs.hhvm.com/s/20cc9b14a8f1c008/images/async/async-slow-curl.png"]

The reordering of different task instructions in this way allow you to hide I/O latency. So while one task is currently sitting at an I/O instruction (e.g., waiting for data), another task's instruction, with hopefully less latency, can execute in the meantime.


## Test results

sync: python 2.7.10 + requests library
async python 3.6 + iohttp with asyncio loop
script: python test

### 1 request
sync: 
```
sync$ time python test.py > /dev/null
0.107u 0.051s 0:00.64 23.4% 0+0k 0+0io 0pf+0w
```

async
```
async$ time python test.py > /dev/null
0.195u 0.049s 0:00.68 30.8% 0+0k 0+0io 0pf+0w
```

for 1 request we won't see any big difference and sometimes async operation can takes even more time to execute, but lets check on 10 iterations

### 10 requests

sync:
```
sync$ time python test.py 10 > /dev/null
0.451u 0.065s 0:05.50 9.2%  0+0k 0+0io 0pf+0w
```

async:
```
async$ time python test.py 10 > /dev/null
0.218u 0.031s 0:01.77 13.5% 0+0k 0+0io 0pf+0w
```

Here we can see that async execution finished in 2 sec versus traditional method that finished in 6 sec

### 1000 requests

sync:
```
sync$ time python test.py 1000 > /dev/null
37.998u 1.166s 9:31.52 6.8% 0+0k 0+0io 277pf+0w
```

async:
```
async$ time python test.py 1000 > /dev/null
2.221u 0.231s 2:03.71 1.9%  0+0k 49+0io 695pf+0w
```

Almost 10 min vs 2 min

Now, lets say we have real application with millions requests per day. The payoff is obvious
