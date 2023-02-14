https://www.codekarle.com/system-design/Notification-system-design.html

![](../pics/Notification.png)

 Kafka -> sms handler, email handler, in-app notification handler

rate limit that uses Redis to have key-value paris for limited notification requests

tracker: Cassandra
