1. 视频网站，任务是生成视频subtitle。现在只有一个机子一个process在工作，然后crash了。问有没有什么work around？ - 说可以多个机子一起process，或者用message asynchronously process，感觉答得不是很好


2. 有100,000个贩卖机分布全球，目前每天凌晨往server报status，然后有个job每天1AM处理status然后依此决定哪些要refill，问这样有什么问题 - 说全球机器同时发会造成拥堵，其它时候又是空闲的，感觉不合理。可以一天多几次report的时间，然后根据地域report时间段不同。

3. 用户储存photo的网站。目前是根据用户名来shard，问有什么问题 - 说会造成分布不均匀。问怎么解决 - 说了consistent hashing



https://productive-horse-bb0.notion.site/Roblox-Karat-2021-5-2022-2-9b07dcbba3634de080c3854c1293d0dc
