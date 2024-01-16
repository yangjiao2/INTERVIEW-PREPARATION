"""
Problem Description:

Imagine we are building an application that is used by many different customers. We want to avoid one customer being able to overload the system by sending too many requests, so we enforce a per-customer rate limit. The rate limit is defined as:

“Each customer can make X requests per Y seconds”
"""

# per-customer rate limit: 10 requests per 5 seconds
# tocken bucket, leaky bucket, fixed window, sliding window


import time, math
class TokenBucket:
    def __init__(self, rate, frame):
        self.rate = rate
        self.frame = frame
        self.last_time = time.time()
        self.token = rate
        
    def _refill(self):
        now = time.time()
        new_token = 0
        diff = (now - self.last_time)
        # print ("diff", diff, self.frame <= diff)
        if self.frame <= diff:
            new_token = int(math.ceil(diff % self.frame)) * self.rate
            # print ("new", new_token,  self.rate)
        self.token = min(self.rate, self.token + new_token)
        # print ("self.token", self.token, new_token)
        self.last_time = now
        
    def rate_limit(self): # boolean
        self._refill()
        if self.token >= 1:
            self.token -= 1
            return True
        return False
        
    
class Customer:
    def __init__(self):
        self.policy = {}
    
    def add_policy(self, customer_id, rate, frame):
        self.policy[customer_id] = {
            "rate": rate,
            "frame": frame,
        }
        
    def get_rate(self, customer_id):
        return self.policy[customer_id]["rate"]
    
    def get_frame(self, customer_id):
        return self.policy[customer_id]["frame"]
        

class RateLimiter:
    def __init__(self, rate, frame):
        self.customer_bucket = {}
        self.customer = Customer()
        self.rate = rate
        self.frame = frame

        
    def consume(self, customer = "default"):
        if customer in self.customer_bucket:
            bucket = self.customer_bucket[customer]
        else:
            self.customer.add_policy(customer, 10, 2)
            self.customer_bucket[customer] = TokenBucket(self.rate, self.frame)
            bucket = self.customer_bucket[customer]
        return bucket.rate_limit()


max_request = 10
frame = 2

rate_limiter = RateLimiter(max_request, frame)
for i in range(35):
    if i == 11:
        time.sleep(2)
        print ("sleep--")
    result = rate_limiter.consume()
    print (result)

# space O(customer)
# time O(1)
