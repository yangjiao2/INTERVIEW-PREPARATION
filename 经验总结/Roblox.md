cold start

engagement and retention: frontier for discovery

monetization

- ml: recommended for you

search and discovery:

- new content


System design  - key value store
考点是write ahead log





系统设计：game matching system，1M DAU, 100k games。user选择加入游戏后，进入到waiting room，系统根据user skill来安排相近level的users组局，组局成功后直接开始游戏；另外，要求每个user最多等待5分钟，否则立马开始游戏。user skill可以通过一个API获得，0-100。这道题，刚开始面试官的要求给得很模糊，反反复复折腾才搞明白到底要设计怎样的系统，耽误了不少时间，matching algorithm这块也没有来得及好好想想。这轮面得不太好，感觉也挺难的。
- 系统设计：To-do list system, 允许users相互share，共同编辑。这轮应该没问题。


design a payment hold system。面试官还是挺友好的。聊的也比较顺利。设计完了以后问了几个问题。首先问了一下如何处理错误，每一个service down了会有什么影响（比如DB挂了怎么办）。第二个问题是问怎么scale。说现在traffic变成了原‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌来的10倍了，你这个系统能不能扛住


system design：经典面筋题todo list，需要注意点：1. qps非常高。2. 因为是shared所以需要考虑multiple user的auth的component/api的设计 感觉面试官本身也不是很懂系统设计，就按套路走就行，全程我在drive meeting
todolist要share给不同的人，所以需要manage acess


creative round: game match。roblox主要是social game，不是competive game，建议着重考虑social属性。考虑多个地区的人language，culture差异。
