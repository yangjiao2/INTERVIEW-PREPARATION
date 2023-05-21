[link](https://towardsdatascience.com/system-design-analysis-of-instagram-51cd25093971)

![](../pics/instagram-design.png)
Functional requirement:
- read, search
- upload
- follow
- display feed

Non func:
- available over consistency
- low latency (200ms on home page)
- reliable

Data flow:
```
Table Name : table indexe1,index2 etc

Photo: PhotoID (pk), UserID, PhotoLocation, CreationDate

User: UserID(pk), Name, Email, DOB, LastLoginTime

Follow: UserID1, UserID2 (paired pk)

FeedItem: FeedID(pk), UserID,Contents, PhotoID,CreationDate

**pk = primary key
```

Push / Pull:
hot key vs. active user


---
https://instagram-engineering.com/making-instagram-com-faster-part-1-62cc0c327538


1) prefetching data

intelligent pre-loading JavaScript and preloading XHR GraphQL requests for data
Approach 1: Have preload tag after the critical `<script>`
```js
<link rel="preload" href="my-js-file.js" as="script" type="text/javascript" />

// js
<link rel="preload" href="/static/FeedPageContainer.js" as="script" type="text/javascript" />

// graphql
<link rel="preload" href="/graphql/query?id=12345" as="fetch" type="application/json" />


```

image:
using the img `srcset` attribute, dimension is determined up to the browser

resources in general:
fetch in prority order,  queueing of asynchronous work which differs in heading of post list, scroll to the bottom of post list

2) improving performance by pushing data directly to the client rather than waiting for the client to request the data

Pushing data early
HTTP Chunked Transfer: This can split the HTML response and has universal support (as compared to complex HTTP/2 push). Every platform has some kind of streaming response library - use that.
Push response/cache first approach: This implementation is a bit involved and custom. For general websites, my gut feel is that a ServiceWorker based approach would work.


3) cache-first rendering (display stale feed data)

1/ load cached result first to user, then create a stage subset of Redux state
2/ store actions while request/push is pending, apply action to new data in the pending state
3/ staged state completes, replace current one

1)

Approach 2: (implemented by Instagram) Use preload for all critical tags and order them in the order it is necessary.
preloading images:
Preload images when the browser is free. This can be done by using the requestIdleCallback API. (There is more to this but, this is a good start)
For the lazy-loaded images, load it sequentially so that the image closes to viewport gets rendered first.
