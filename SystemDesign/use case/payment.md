### Retry and Idempotency

![](../pics/payment.jpeg)

idempotency

 uber有个分布式的实现，不怎么详细，airbnb有个非常详细的SQL sharding的实现

SQL sharding

https://newsletter.pragmaticengineer.com/p/designing-a-payment-system

![](../pics/payment.webp)


A credit card requires extra protection like 3D Secure Authentication [13] which requires extra details from a card holder to verify a purchase.

payment request is finally completed, the PSP calls the registered webhook mentioned above.

poll the PSP for status updates on any pending payment requests. 