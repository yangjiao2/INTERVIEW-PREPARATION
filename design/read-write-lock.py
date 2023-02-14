"""
Lock

# create a lock
lock = Lock()
# acquire the lock
lock.acquire()
    # or
with lock:
    ...

# release the lock
lock.release()

# acquire the lock without blocking
lock.acquire(blocking=false)

"""


import threading

class RWLock(object):
    def __init__(self):
        self.writer_lock = threading.Lock()
        self.num_readers_lock = threading.Lock() #Lock for incrementing and decrementing num_readers
        self.num_readers = 0

    def acquire_reader(self):
        with self.num_readers_lock:
            self.num_readers += 1
            if self.num_readers == 1:
                self.writer_lock.acquire()

    def release_reader(self):
        assert self.num_readers > 0
        with self.num_readers_lock:
            self.num_readers -= 1
            if self.num_readers == 0:
                self.writer_lock.release()

    def acquire_writer(self):
        self.writer_lock.acquire()

    def release_writer(self):
        self.writer_lock.release()



class WritePreferringRWLock:

    def __init__(self):
        self.num_writers_waiting = 0
        self.is_writing = False
        self.writer_lock = threading.Lock()
        self.writer_condition = threading.Condition(self.writer_lock())
        self.num_readers_reading = 0

    def acquire_reader(self):
        with self.writer_lock:
            while self.num_writers_waiting > 0 or self.is_writing:
                self.writer_condition.wait()
                # releases the underlying lock, and
                # then blocks until it is awakened by a notify() or notify_all() call
                # for the same condition variable in another thread
            self.num_readers_reading += 1

    def release_reader(self):
        with self.writer_lock:
            self.numReadersReading -= 1
            if self.num_readers_reading < 0:
                raise Exception("Improper use of lock!")
            if self.num_readers_reading == 0:
                self.writer_condition.notifyAll()

    def acquire_writer(self):
        with self.writer_lock:
            self.num_writers_waiting += 1
            while self.num_readers_reading > 0 or self.is_writing:
                self.writer_condition.wait()
            self.num_writers_waiting -= 1 #available
            self.is_writing = True

    def release_writer(self):
        with self.writer_lock:
            self.is_writing = False
            self.writer_condition.notifyAll()
