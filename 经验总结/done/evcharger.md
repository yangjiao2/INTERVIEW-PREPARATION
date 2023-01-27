```
I'm worried about running into performance issues as our app scales. Can you describe performance optimizations that we should consider?

YJ
Yang Jiao

1. localization: we need to think about the user's localization. For example, our app could expand around the globe. Then we will need to think about adding local servers, databases, and CDNs for reducing data fetching APIs's delay.

2. cache search result, user preference, images: since there are fixed types of charger, charger types and prices, we could use smart ways to pull data (from local cache), if we can assume that that charger types, images, prices is not frequently changed. We could store these info so that when same request fetch on the same category or same charger type, we could fetch from local cache.

3. image resolution: more specifically we should think about how to handle images. Since we have different size of images, we could optimize image loading by providing different resolution. When we are showing the list view, we could have images with low resolution. While after user tap into detail view, we could use better resolution given image size is larger.



TW
Taylor Williams

We need to decide what transition will happen when a user taps on one of the cards. Could you recommend some possible transitions, and explain how they would impact user experience?

YJ
Yang Jiao

1. upon tapping on the card background:
we could make the card to be responsive by making a subtle change on card background. This will improve user experience.

2. upon tapping on the image, we could offer a pop up window with enlarged image so that user could view the image clearly.

3. during loading to detail view, we could use lazy loading on images so that it will not keep user waiting while fetching the image. So we could use a glimmer component as a loading indicator, to suspense and lazy load image.

TW
Taylor Williams

What accessibility best practices do you think we could implement? Please describe them.

YJ
Yang Jiao

1. proper alt text for images (each photo has alt text)
2. use color with contract
3. ensure that all content can be accessed with the keyboard, for keyboard-only or screen readers users
4. use ARIA to label properly, such as roles, aria-label, aria-lebeledby

TW
Taylor Williams

Some clients may have flaky internet connections. Do you have recommendations on how we can help improve the user experience for those cases?

YJ
Yang Jiao

1. cache results: we will try to save results from previous searches as well as user's common location to serve data even user is offline

2. indicator: while having problem loading, we could add a banner to show that the internet is not stable to let user be aware of the results might not be accurate / realtime.


TW
Taylor Williams

What are two or three criteria we might use to sort results? Which would you suggest based on user impact?

YJ
Yang Jiao

criteria:
distance, charger type, price

User care most about these category and would want to compare between results.


TW
Taylor Williams

Which option(s) outlined in “Sorting Results” do you recommend, and why? What are pros, cons, trade-offs, and assumptions that motivated your implementation choice?

```
