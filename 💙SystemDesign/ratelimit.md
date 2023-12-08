计数器法

- 如果计数器的值小于限流值

```    private AtomicInteger requestCount = ZERO;

    //获取限流
    public boolean tryAcquire() {

        long now = System.currentTimeMillis();

        //在时间窗口内
        if (now < startTime + interval) {

            //判断是否超过最大请求
            if (requestCount.get() < limit) {
                requestCount.incrementAndGet();
                return true;
            }
            return false;

        } else {

            //超时重置
            startTime = now;
            requestCount = ZERO;
            return true;
        }

    }
```




漏桶算法

- 速率可控

```


    //获取限流
    public boolean tryAcquire() {

        //执行漏水，更新剩余水量
        refresh();

        //尝试加水，水满则拒绝
        if (water + 1 > capacity) {
            return false;
        }

        water = water + 1;
        return true;

    }

    private void refresh() {
        //当前时间
        long currentTime = System.currentTimeMillis();

        if (currentTime > lastLeakTime) {

            //距上次漏水的时间间隔
            long millisSinceLastLeak = currentTime - lastLeakTime;
            long leaks = millisSinceLastLeak * ratePerMillSecond;

            //允许漏水
            if (leaks > 0) {
                //已经漏光
                if (water <= leaks) {
                    water = 0;
                } else {
                    water = water - leaks;
                }
                this.lastLeakTime = currentTime;
            }
        }
    }

```



令牌桶算法

- 控制留出
- 从桶里移除一个令牌，如果没有令牌的话，请求无法通过
- no burst request allowed

```py

class TokenBucketLimiter:
    def __init__(self, capacity, window_time_in_seconds):
        self.capacity = capacity
        self.window_time_in_seconds = window_time_in_seconds
        self.last_refill_timestamp = int(time.time() * 1000)  # Current time in milliseconds
        self.refill_count_per_second = capacity / window_time_in_seconds
        self.available_tokens = 0

    def get_available_tokens(self):
        return self.available_tokens

    def try_acquire(self):
        # Update the token bucket
        self.refill()

        if self.available_tokens > 0:
            self.available_tokens -= 1
            return True
        else:
            return False

    def refill(self):
        now = int(time.time() * 1000)  # Current time in milliseconds

        if now > self.last_refill_timestamp:
            elapsed_time = now - self.last_refill_timestamp

            tokens_to_be_added = int((elapsed_time / 1000) * self.refill_count_per_second)

            if tokens_to_be_added > 0:
                self.available_tokens = min(self.capacity, self.available_tokens + tokens_to_be_added)
                self.last_refill_timestamp = now

```