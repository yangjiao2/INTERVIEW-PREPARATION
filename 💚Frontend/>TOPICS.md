1. Debounce

```js

/**
 * @callback func
 * @param {number} wait
 * @return {Function}
 */
export default function debounce(func, wait = 0) {
  let timeoutID = null;
  return function (...args) {
    clearTimeout(timeoutID);

    // Has the same `this` as the outer function's
    // as it's within an arrow function.
    timeoutID = setTimeout(() => {
      timeoutID = null; // Not strictly necessary but good to include.


      // func.apply()/func.call() taking first argument as "this" (or context), args are passed in as "args".
      func.apply(this, args);
    }, wait);
  };
}

```

2. Scope and Closures
3. Functions

func.apply(thisArg, args)
func.call(thisArg, ...args)


4. Arrays
5. Objects
6. DOM Manipulation
7. Asynchronous JavaScript
8. AJAX and Fetch API
9. JSON
10. Promises

```js
/**
 * @param {Array} iterable
 * @return {Promise<Array>}
 */
export default function promiseAll(iterable) {
  return new Promise((resolve, reject) => {
    const results = new Array(iterable.length);
    let unresolved = iterable.length;

    if (unresolved === 0) {
      resolve(results);
      return;
    }

    iterable.forEach(async (item, index) => {
      try {
        // option1 is to use `await` which requires async function call
        const value = await item;
        // option2 is to use `.then` to solve values
        results[index] = value;
        unresolved -= 1;

        if (unresolved === 0) {
          resolve(results);
        }
      } catch (err) {
        reject(err);
      }
    });
  });
}
```


11. Callback Functions
12. ES6+ Features
13. Template Literals
14. Destructuring
15. Spread and Rest Operators
16. Arrow Functions
17. Classes and Prototypes
18. Timeout

```js
function customInterval(callback, interval) {
  let timerId;

  function repeat() {
    callback();
    timerId = setTimeout(repeat, interval);
  }

  repeat();

  // Return the cancellation function
  return function cancel() {
    clearTimeout(timerId);
  };
}

// Example usage:
const cancelInterval = customInterval(() => {
  console.log('This is repeated every 1000 ms');
}, 1000);

// To cancel the interval after some time (e.g., 5000 ms):
setTimeout(() => {
  cancelInterval();
  console.log('Interval canceled after 5000 ms');
}, 5000);

```
19. Event Handling
20. Event Bubbling and Delegation
21. Promises
22. Local Storage and Session Storage
23. Cookies
24. Error Handling
25. Regular Expressions
26. Functional Programming
27. Map, Filter, and Reduce
28. Higher-Order Functions
29. Callback Hell

36. Cross-Origin Resource Sharing (CORS)
37. Same-Origin Policy
38. Security Best Practices
39. HTTPS
40. WebSockets
41. Progressive Web Apps (PWAs)
42. Responsive Web Design
43. Flexbox
44. CSS Grid

48. API Design and RESTful APIs
49. GraphQL
50. Design Patterns