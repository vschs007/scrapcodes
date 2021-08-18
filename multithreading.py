from threading import  *
from time import sleep


class hello(Thread):
    def run(self):
        for i in range(10):
            print("hello")


class hi(Thread):
    def run(self):
        for i in range(10):
            print("hi")


t1 = hello()
t2 = hi()

t1.start()
t2.start()

t1.join()
t2.join()
print("threading finished")