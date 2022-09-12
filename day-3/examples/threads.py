# primer on threading
# https://realpython.com/intro-to-python-threading/

from threading import Thread
import time

res = 0


def myfunc(num):
    global res

    for i in range(5):
        print("From thread", num)
        time.sleep(1)
    res = num


th1 = Thread(target=myfunc, args=['111'])
th1.start()

for i in range(3):
    print("from main", i)
    time.sleep(1)

th1.join()
print("end", res)
