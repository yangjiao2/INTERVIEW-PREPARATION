
 https://stripe.com/blog/idempotency
idempotency keys (unique ID on server): guaranteeing that side effects only occur once.

 “double-charge” problem: failure on
 - 1) client -> retry
 - 2) server -> Database ACID to retry
 - 3) server ack -> replies with a cached result of the successful operation. (it simply ignores the request and responds with a successful status code.)
 -

 thundering herd problem: too many retry -> exponential backoff and random jitter

from stripe
```py
def self.sleep_time(retry_count)
  # Apply exponential backoff with initial_network_retry_delay on the
  # number of attempts so far as inputs. Do not allow the number to exceed
  # max_network_retry_delay.
  sleep_seconds = [Stripe.initial_network_retry_delay * (2 ** (retry_count - 1)), Stripe.max_network_retry_delay].min

  # Apply some jitter by randomizing the value in the range of (sleep_seconds
  # / 2) to (sleep_seconds).
  sleep_seconds = sleep_seconds * (0.5 * (1 + rand()))

  # But never sleep less than the base sleep seconds.
  sleep_seconds = [Stripe.initial_network_retry_delay, sleep_seconds].max

  sleep_seconds
end

```



ACID is an acronym of Atomicity, Consistency, Isolation and Durablity.

Atomicity means transaction either completes or fails in entirety. There is no state in between. No body sees a partial completion of a transaction.

Consistency means the transaction leaves the database in the valid state.

Isolation means no two transactions mingle or interfere with each other. The result of two transactions executed in parallel would be same as sequential execution.

Durability means the changes of the transaction are saved. It remains there even if power is turned off.





Shopify:
order is in sequential with unique UUID
