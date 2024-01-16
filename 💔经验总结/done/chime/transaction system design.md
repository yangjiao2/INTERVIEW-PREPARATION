trade off我能想到的
1. 用户transfer一次后要记忆之前的default transfer option，如果从来没用过这功能的话讨论default as chime to other vs other to chime（UX角度出发，没从tech）
2. mobile端要不要一个单独的rule service vs 这些rule全由后端的permission check来做然后cache到mobile（UX角度和tech都有聊，比如让user点transfer了等一会儿才告诉check没过，那会很沮丧，而且从network角度来讲会过多request）
3. 怎么scale rule service，我用的是mimic后端常见的attribute（rule）based permission mode‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌l。所有page只是询问rule serivce by passing in 要做啥，和entity ids。rule可以把permission check结果和rule直接cache在前端的realmDB
4. rule in sync, 如果mobile也写一些简单的rule service的一个问题是如果多了，前后端可能不sync。这样的话其实可以后端写一份然后用codegen，确保改动只在一处
5. team ownership，这个rule service尽管mobile和backend都有，但应该是一个team来own。给partner team开放codegen和api to check rule就好
6. Metric，north star定transfer amout vs frequency。从product sense角度我认为应该定frequency。topline才定amount和transfer in vs out
6. 没讨论UI，感觉不是intresting point to discuss