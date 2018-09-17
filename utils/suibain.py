import time

def deco(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        msg = (endtime - starttime) * 1000
        print("time is %d ms" %msg)
    return wrapper

@deco
def func():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':
    f = func
    f()
    if None:
        print('hi')
    for i in range(1, 3):
        print(i)
