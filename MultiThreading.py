# WHAT IS MULTI-TASKING ?
'''
- The process of multi-tasking lets a CPU execute various tasks at the very same time.
- CPU switching occurs very often when multitasking between various tasks. Since it involves rapid CPU switching, it
  requires some time. It is because switching from one user to another might need some resources.
'''

# WHAT IS MULTI-THREADING ?
'''
- It is a system that creates many threads out of a single process to increase the overall power and working capacity 
  of a computer.
- In the process of multi-threading, we use a CPU for executing many threads out of a single process at any given time.
- Thread is subset of process or we can say thread is a light weight process or we can say thread nothing but part of 
  process.
- Default thread is a main thread because it is responsible to execute the process.
- Dependancy is not allowed in multi-threading.
'''

# When to use Multi-Threading ?
'''
- It is a very useful technique for time-saving and improving the performance of an application.
- Multithreading allows the programmer to divide application tasks into sub-tasks and simultaneously run them in a program.
- It allows threads to communicate and share resources such as files, data, and memory to the same processor.
'''

# Benefits of Multi-Threading
'''
1. It ensures effective utilization of computer system resources.
2. It saves time by executing multiple threads at the same time.
3. The system does not require too much memory to store multiple threads.
'''


# JOIN() method:
'''
- It is a join() method used in the thread class to halt the main thread's execution and waits till the complete 
  execution of the thread object. When the thread object is completed, it starts the execution of the main thread in Python.
- A join() method is used to block the execution of another code until the thread terminates.
'''

# START() method:
'''
- To start a thread in Python multithreading, call the thread class's object. The start() method can be called once for 
  each thread object; otherwise, it throws an exception error.
- A start() method is used to initiate the activity of a thread. And it calls only once for each thread so that the 
  execution of the thread can begin.
'''



# 1. CREATING THREAD WITHOUT USING ANY CLASS (function base threading)

'''
import threading

print(threading.current_thread())
print(threading.current_thread().name)
print(threading.main_thread())
print(threading.main_thread().name)

def add():
    a = 5
    b = 50
    print(a+b)
add()
print("Addition Done")
'''

# EXAMPLE: 1
'''
import threading

def add():
    a = 5
    b = 50
    print(a+b)
# add()
print("Addition Done")

t1 = threading.Thread(target=add())
t1.start()

print("Threading Operation Done")
'''

# EXAMPLE: 2
'''
import threading

def add():
    a = 5
    b = 50
    print(a+b)
    for i in range(5):
        print("Hii")

t1 = threading.Thread(target=add())
t1.start()

for j in range(5):
    print("Bye")
'''

# EXAMPLE: 3
'''
import threading

def add():
    a = 5
    b = 50
    print(a+b)
    for i in range(5):
        print("Hii")

def C1():
    print("Check")

t1 = threading.Thread(target=add())
t1.start()

t2 = threading.Thread(target=C1())
t2.start()

for j in range(5):
    print("Bye")
'''

# EXAMPLE: 3
'''
import threading

def add():
    a = 5
    b = 50
    print(a+b)
    for i in range(5):
        print("Hii")

t1 = threading.Thread(target=add())
t1.start()

def C1():
    print("Check")

t2 = threading.Thread(target=C1())
t2.start()

for j in range(5):
    print("Bye")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2. CREATING THREAD BY EXTENDING THREAD CLASS

# EXAMPLE: 1
'''
from threading import Thread

class Check(Thread):
    def run(self):
        for i in range(5):
            print("Hii")

t1 = Check()
t1.start()

for i in range(10):
    print("Bye")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 3. CREATING THREAD WITHOUT EXTENDING THREAD CLASS

# EXAMPLE: 1
'''
from threading import Thread

class Check:
    def m1(self):
        for i in range(5):
            print("Child")
    def m2(self):
        for j in range(10):
            print("Parent")

obj = Check()
a = Thread(target=obj.m1())
b = Thread(target=obj.m2())
'''

# EXAMPLE: 2
'''
from threading import Thread

class Check:
    def m1(self):
        for i in range(5):
            print("Child")
    def m2(self):
        for j in range(10):
            print("Parent")

obj = Check()
t1 = Thread(target=obj.m1())
t2 = Thread(target=obj.m2())
t1.start()
t2.start()
'''

# EXAMPLE: 3 -With Multi-Threading
'''
from threading import Thread
import time

class Check:
    def m1(self):
        for i in range(5):
            print("Child")
            time.sleep(1)

    def m2(self):
        for j in range(5):
            print("Parent")
            time.sleep(1)

StartTime = time.time()
obj = Check()
t1 = Thread(target=obj.m1())
t2 = Thread(target=obj.m2())
print("Total time required: ", time.time()-StartTime, "sec")
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻