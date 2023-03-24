from multiprocessing import Process
import time
def countdown(name, delay, count):
      while count:
          time.sleep(delay)
          print (f'{name, time.ctime(time.time()), count}')
          count -= 1
class newProcess(Process):
      def __init__(self, name, count):
          Process.__init__(self)
          self.name = name
          self.count = count
      def run(self):
          print("Starting: " + self.name + "\n")
          countdown(self.name, 0, self.count)
          print("Exiting: " + self.name + "\n")
t = newProcess("newProcess 1", 5)
t.start()
t.join()
print("Done")
