# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# each worker takes 1 min per stage

from heapq import heappush, heappop, heapify


class Task:
    def __init__(self, name, duration={0: 1, 1: 1, 2:1}):
        self.name = name
        self.duration = duration
        self.history = set()
        self.stage = 0
        
    def __lt__(self, other):
        if not isinstance(other, type(self)): 
            return self < other
        # p1 < p2 calls p1.__lt__(p2)
        return self.name < other.name
    
    def __eq__(self, other):
        # if not isinstance(other, type(self)): 
        #     return self == other
        # p1 == p2 calls p1.__eq__(p2)
        return self.name == other.name
        
    def proceed(self):
        self.duration[self.stage] -= 1
        # if (not self.is_task_complete()):
        # print ('proceed', self.name, self.duration, self.duration[self.stage] == 0 , self.stage)
        if self.is_task_complete():
            return -1
        elif self.is_stage_complete():
            self.stage += 1
            return 0
            
        return 1
        
    def time_required_by_next_stage(self):
        if (not self.is_task_complete()):
            return self.duration[self.stage]
            
        return None
    
    def assign_to_worker(self, worker):
        self.history.add(worker.name)
        # self.proceed()
        
    def is_stage_complete(self):
        return self.duration[self.stage] == 0 and self.stage != (len(self.duration) - 1)
    
    def is_task_complete(self):
        return self.duration[self.stage] == 0 and self.stage == (len(self.duration) - 1)
        
        
class Worker:
    def __init__(self, name):
        self.name = name
        self.task = None
#         # self.task_start_time = None
#         # self.task_end_time = None
#         
    def assign_task(self, task):
        print(f"Assigning {self.name} to Task {task.name} for L{task.stage}")
        self.task = task
        self.task.assign_to_worker(self)
    
    def finish_task(self):
        print(f"Worker {self.name} finished Task {self.task.name} for L{self.task.stage - 1}")
        self.task = None
        
class Scheduler:
    def __init__(self, tasks, workers):
        self.time = 0
        self.queue = []
        self.worker = workers
        for task in tasks:
            self.add_task(task)
        self.count = len(tasks)
        
    def add_task(self, task):
        # self.queue.append(task)
        time_required = task.time_required_by_next_stage()
        # print ('add_task', self.queue, task.name)
        self.queue.append((-time_required, task))
        
    def add_worker(self, worker):
        self.worker.append(worker)
        
    def time_lapse(self):
        print(f"Time: {self.time}")
        self.time += 1
        
        idle_worker = []
        for worker in self.worker:
            # print ('!', worker.name, [q for q in self.queue])
            if worker.task:
                next_state = worker.task.proceed()
                # print (1, worker.task.name, next_state)
                
                if next_state == -1: ## stage complete or task complete
                    worker.finish_task()
                    self.count -= 1
                    # idle_worker.append(worker)
                elif next_state == 0:
                    self.add_task(worker.task)
                    worker.finish_task()
                    # idle_worker.append(worker)
                else:
                    continue

            
            idle_worker.append(worker)
         
        for worker in idle_worker:
            if len(self.queue) != 0:
                [_time, new_task] = heappop(self.queue)
                # print ('new_task.name', new_task.name)
                worker.assign_task(new_task)
            
        heapify(self.queue)

    def start(self):
        while self.count:
            # print ('++', self.queue, self.count)
            self.time_lapse()
        


tasks = [Task('A')]
workers = [Worker('X'), Worker('Y'), Worker('Z')]
s1 = Scheduler(tasks, workers)
s1.start()

# tasks = [Task('A',{0: 1, 1: 2, 2:8}), Task('B', {0: 1, 1: 8, 2:3}), Task('C', {0: 1, 1: 1, 2:1}) ]
# workers = [Worker('X'), Worker('Y')]
# s2 = Scheduler(tasks, workers)
# s2.start()

# print (Task('A',{0: 1, 1: 2, 2:8}) <  Task('B', {0: 1, 1: 8, 2:3}))




