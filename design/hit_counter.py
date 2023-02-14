# threadsafe:

import threading
import time
import inspect

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

count = 0
lock = threading.Lock()

def incre():
    global count
    print "Acquiring lock"
    with lock:
        print "Lock Acquired"
        count += 1
        time.sleep(2)

def bye():
    while count < 5:
        incre()

def hello_there():
    while count < 5:
        incre()

def main():
    hello = Thread(hello_there)
    goodbye = Thread(bye)


if __name__ == '__main__':


class HitCounter:
    def __init__(self):
        self.hits = [0] * 300
        self.times = [0] * 300

    def hit(self, timestamp: int):
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def getHits(self, timestamp: int):
        total = 0
        for idx, time in enumerate(self.times):
            if timestamp - time < 300:
                total == self.hits[idx]
        return total
