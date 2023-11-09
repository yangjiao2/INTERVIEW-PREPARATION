Coding Round
Question 1 : API Rate Limiter
Question 2: Extend the rate limiter to account different limits for different users
Question 3: Extend the rate limiter to apply something like carrying forward the balance.


## Token Bucket Algorithm:

Pros:

Allows bursts of requests within the capacity limits.
Provides smooth and controlled rate limiting.
Can handle short bursts of traffic.

Cons:

Requires periodic token replenishment.
May result in tokens going unused if not consumed.


## Leaky Bucket Algorithm:

Pros:

Allows bursts of requests within the capacity limits.
Can be more memory efficient compared to Token Bucket.
Provides a constant and predictable rate limiting.

Cons:

Tokens are leaked at a constant rate, which can result in unused tokens.


## Sliding Window Algorithm:

Pros:

Provides a fixed and predictable rate limiting.
No need for token management or leaking.
Can adapt more quickly to changes in traffic.

Cons:

Limited by the size of the window, which can lead to less flexibility in handling bursts.


----


import time

class TokenBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill_time = time.time()
        self.rate = rate

    def _refill_tokens(self):
        now = time.time()
        delta_time = now - self.last_refill_time
        tokens_to_add = delta_time * self.rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = now

    def request_token(self):
        self._refill_tokens()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

class LeakyBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.tokens = 0
        self.last_leak_time = time.time()
        self.rate = rate

    def _leak_tokens(self):
        now = time.time()
        delta_time = now - self.last_leak_time
        tokens_to_leak = delta_time * self.rate
        self.tokens = max(0, self.tokens - tokens_to_leak)
        self.last_leak_time = now

    def request_token(self):
        self._leak_tokens()
        if self.tokens < self.capacity:
            self.tokens += 1
            return True
        else:
            return False

token_buckets = {}
leaky_buckets = {}

def rateLimitTokenBucket(customer_id):
    if customer_id not in token_buckets:
        user_limits = {
            "customer_1": (10, 2),
            "customer_2": (20, 5),
            "customer_3": (5, 1),
            # Add more customers and their limits as needed
        }
        if customer_id in user_limits:
            capacity, rate = user_limits[customer_id]
            token_buckets[customer_id] = TokenBucket(capacity=capacity, rate=rate)
        else:
            token_buckets[customer_id] = TokenBucket(capacity=10, rate=2)

    return token_buckets[customer_id].request_token()

def rateLimitLeakyBucket(customer_id):
    if customer_id not in leaky_buckets:
        user_limits = {
            "customer_1": (10, 2),
            "customer_2": (20, 5),
            "customer_3": (5, 1),
            # Add more customers and their limits as needed
        }
        if customer_id in user_limits:
            capacity, rate = user_limits[customer_id]
            leaky_buckets[customer_id] = LeakyBucket(capacity=capacity, rate=rate)
        else:
            leaky_buckets[customer_id] = LeakyBucket(capacity=10, rate=2)

    return leaky_buckets[customer_id].request_token()

customer_ids = ["customer_1", "customer_2", "customer_3", "customer_4"]

for customer_id in customer_ids:
    token_result = rateLimitTokenBucket(customer_id)
    leaky_result = rateLimitLeakyBucket(customer_id)
    print(f"Token Bucket Algorithm Result for {customer_id}: {token_result}")
    print(f"Leaky Bucket Algorithm Result for {customer_id}: {leaky_result}")

---

import time

class Bucket:
    def __init__(self, capacity, rate, algorithm):
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill_time = time.time()
        self.rate = rate
        self.algorithm = algorithm

    def _refill_tokens(self):
        now = time.time()
        delta_time = now - self.last_refill_time
        tokens_to_add = delta_time * self.rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = now

    def request_token(self):
        if self.algorithm == "Token":
            self._refill_tokens()
        elif self.algorithm == "Leaky":
            self._leak_tokens()

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

    def _leak_tokens(self):
        now = time.time()
        delta_time = now - self.last_refill_time
        tokens_to_leak = delta_time * self.rate
        self.tokens = max(0, self.tokens - tokens_to_leak)
        self.last_refill_time = now

def rateLimitBucket(customer_id, algorithm):
    if customer_id not in buckets:
        user_limits = {
            "customer_1": (10, 2),
            "customer_2": (20, 5),
            "customer_3": (5, 1),
            # Add more customers and their limits as needed
        }
        if customer_id in user_limits:
            capacity, rate = user_limits[customer_id]
            buckets[customer_id] = Bucket(capacity=capacity, rate=rate, algorithm=algorithm)
        else:
            buckets[customer_id] = Bucket(capacity=10, rate=2, algorithm=algorithm)

    return buckets[customer_id].request_token()

buckets = {}

customer_ids = ["customer_1", "customer_2", "customer_3", "customer_4"]

for customer_id in customer_ids:
    token_result = rateLimitBucket(customer_id, "Token")
    leaky_result = rateLimitBucket(customer_id, "Leaky")
    print(f"Token Bucket Algorithm Result for {customer_id}: {token_result}")
    print(f"Leaky Bucket Algorithm Result for {customer_id}: {leaky_result}")


---

import queue
import threading
import time

# Create a queue to hold the tasks
task_queue = queue.Queue()

# Define a function that processes tasks
def process_task(task):
    print(f"Processing task: {task}")
    # Add your task processing code here

# Define a worker function that continuously processes tasks
def worker():
    while True:
        try:
            task = task_queue.get(timeout=1)  # Wait for up to 1 second for a task
            process_task(task)
            task_queue.task_done()
        except queue.Empty:
            pass

# Create a thread for the worker
worker_thread = threading.Thread(target=worker)
worker_thread.daemon = True
worker_thread.start()

# Add tasks to the queue
for i in range(5):
    task_queue.put(f"Task {i}")

# Wait for the tasks to be processed
task_queue.join()

print("All tasks processed")


import time
from multiprocessing import Process, Lock

class TokenBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill_time = time.time()
        self.rate = rate
        self.lock = Lock()

    def _refill_tokens(self):
        now = time.time()
        delta_time = now - self.last_refill_time
        tokens_to_add = delta_time * self.rate
        with self.lock:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_time = now

    def request_token(self):
        with self.lock:
            self._refill_tokens()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                return False

def rateLimitTokenBucket(customer_id):
    if customer_id not in token_buckets:
        token_buckets[customer_id] = TokenBucket(capacity=10, rate=2)

    return token_buckets[customer_id].request_token()

token_buckets = {}

def process_function(customer_id):
    result = rateLimitTokenBucket(customer_id)
    print(f"Token Bucket Algorithm Result for {customer_id}: {result}")

if __name__ == '__main__':
    customer_ids = ["customer_1", "customer_2", "customer_3", "customer_4"]

    processes = []
    for customer_id in customer_ids:
        process = Process(target=process_function, args=(customer_id,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()



import time
from multiprocessing import Process, Lock

class TokenBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill_time = time.time()
        self.rate = rate
        self.lock = Lock()

    def _refill_tokens(self):
        now = time.time()
        delta_time = now - self.last_refill_time
        tokens_to_add = delta_time * self.rate
        with self.lock:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_time = now

    def request_token(self, customer_id):
        with self.lock:
            self._refill_tokens()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                return False

token_buckets = {}

def rateLimitTokenBucket(customer_id):
    if customer_id not in token_buckets:
        # Define different limits for different users here
        user_limits = {
            "customer_1": (10, 2),
            "customer_2": (20, 5),
            "customer_3": (5, 1),
            # Add more customers and their limits as needed
        }
        if customer_id in user_limits:
            capacity, rate = user_limits[customer_id]
            token_buckets[customer_id] = TokenBucket(capacity=capacity, rate=rate)
        else:
            # Default values if customer not found in user_limits
            token_buckets[customer_id] = TokenBucket(capacity=10, rate=2)

    return token_buckets[customer_id].request_token(customer_id)

def process_function(customer_id):
    result = rateLimitTokenBucket(customer_id)
    print(f"Token Bucket Algorithm Result for {customer_id}: {result}")

if __name__ == '__main__':
    customer_ids = ["customer_1", "customer_2", "customer_3", "customer_4"]

    processes = []
    for customer_id in customer_ids:
        process = Process(target=process_function, args=(customer_id,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
