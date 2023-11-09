
1. Coding 给一个字符串数组和一个target字符串，求通过字符串数组构建这个字符串的方式数
2. rate limiting，半算法design 半coding
3. tag management system, design
4. Behavior question + project deepdive
5. Design snake game



rate limit，tag design， file sort。




Round 2: Code Design - rate limiter
Round 3: System design - design tagging system


我目前在想可以用nosql database，然后每当user加一个tag就同时存到两个table，一个是DocumentByTag（partition key是tag id，sort key是document id），一个是TagByDocument（partition key是document id，sort key是tag id），这样就能实现用tag search documents，或者用document search tags。但不知道这是不是一个正确的思路。感谢楼主指教！
 
就存相同的数据存两遍 然后用hash算法split到不同的node里面


体验很好 印度大姐不断问follow up 直到把我考倒了 然后心满意足的结束:
问的大概是要设计一个database 讨论了一下不同sharding的情况 然后需要在分布式的情况下 利用tag id search document, 同时又可以通过document id search tags.  


top k largest element




地里经典的tagging system，我之前准备了一些elastic search的相关内容，基本都是按准备的说的，但面试官似乎不是很懂，我就穿插着给他讲了一些es 的实现，因为我从一开始就没往别的方向聊，所以面试官基本就围绕es 问的 deep dive的问题
第二天 round1 Code design interview, 我本来按地理的面经准备了好几个rate limiter，结果面试官让我写一个贪吃蛇的游戏,leetcode上有这个题，写完，测试完，感觉这个面试官很随和（当然完全可能是假象）
round 2 data structure interview，设计‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌一个投票的数据结构，然后写一个找出排名的功能，类似莉蔻 以伞溜溜，但是要设计专门的投票数据结构，记分方式是第一名3分第二名2分第三名1分，我用了个hashmap统计了所有的分然后不会写sort hashmap by value，最后经过面试关许可在网上找的，输出了正确的结果，但我觉得我做的非常的烂
