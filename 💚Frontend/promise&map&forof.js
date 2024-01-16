Do not use forEach with async-await
TLDR: Use for...of instead of forEach in asynchronous code.

Because forEach does not wait for each promise to resolve, all the prizes are awarded in parallel, not serial (one by one).
So the loop actually finishes iterating before any of the prizes have finished being awarded! (But after they have all started being awarded).


await Promise.all(players.map(async (player) => {
  await givePrizeToPlayer(player);
}));
This will start awarding all the prizes at once, but it will wait for all of them to complete before proceeding to sendEmailToAdmin().

(In the example above you could use return instead of the second await, or indeed use players.map(givePrizeToPlayer). But the pattern shown above can be useful in general situations.)



Process each player in serial, using Array.prototype.reduce
Some people recommend this approach:

await players.reduce(async (a, player) => {
  // Wait for the previous item to finish processing
  await a;
  // Process this item
  await givePrizeToPlayer(player);
}, Promise.resolve());
(We are using the accumulator a not as a total or a summary, but just as a way to pass the promise from the previous item's callback to the next item's callback, so that we can wait for the previous item to finish being processed.)

This has pretty much the same behaviour as the for...of above, but is somewhat harder to understand.


TLDR: Only map(), reduce(), flatMap() and reduceRight() if used correctly


But most array functions will not give us a promise back, or allow a promise to be passed from one call to the next, so they cannot be used asynchronously. So, for example, you can not use asynchronous code inside array.some() or array.filter():

// BAD
const playersWithGoodScores = await players.filter(async (player) => {
  const score = await calculateLatestScore(player);
  return score >= 100;
});
It might look like that should work but it won't, because filter was never designed with promises in mind. When filter calls your callback function, it will get a Promise back, but instead of awaiting that promise, it will just see the promise as "truthy", and immediately accept the player, regardless of what their score will eventually be.

function testPromise(time) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(`Processing ${time}`);
      resolve(time);
    }, time);
  });
}

/*
  For of loop: unpack items from array and execute async function in input order with main thread blocking for each.
  This is conceptually same as Array.reduce (which listed down below).
*/

let timeouts = [3000, 2000, 1000, 4000];
let results = [];
const start = Date.now();

// Define an async function to use await inside the loop
async function processTimeouts() {
  for (const nextTimeout of timeouts) {
    try { 
      // Use await inside the loop to wait for each promise to resolve
      const result = await testPromise(nextTimeout); logger(result, Date.now() - start);
      results.push(result);
    } catch (error) {
      console.error("Error:", error);
    }
  }

  // Log the results and total time after all promises are resolved
  logger(results, Date.now() - start);
  console.log("All Promises Resolved !!✨", results);
}

processTimeouts()


/*
  Result output:

Processing 3000
3000 finished waiting 3 seconds later.
Processing 2000
2000 finished waiting 5 seconds later.
Processing 1000
1000 finished waiting 6 seconds later.
Processing 4000
4000 finished waiting 10 seconds later.
3000,2000,1000,4000 finished waiting 10 seconds later.
All Promises Resolved !!✨ (4) [3000, 2000, 1000, 4000]
*/




/*
  For of loop + Promise.all: unpack items from array and execute simulataenously and 
  result will be arranged in order👍.
  This is conceptually same as Array.map (which listed in the next block.
*/

let timeouts = [3000, 2000, 1000, 4000];
let results = [];
const start = Date.now();


// Use for...of loop to iterate over timeouts and create promises
for (const nextTimeout of timeouts) {
  promises.push(testPromise(nextTimeout));
}

// Use Promise.all to wait for all promises to resolve
Promise.all(promises)
  .then((results) => {
    logger(results, Date.now() - start);
    console.log("All Promises Resolved !!✨", results);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

/*
  Result output:

Processing 1000
Processing 2000
Processing 3000
Processing 4000
3000,2000,1000,4000 finished waiting 4 seconds later.
All Promises Resolved !!✨ (4) [3000, 2000, 1000, 4000]
*/ 



/*
  Array map: this maps async promises in an array and we can use Promise.all or Promise.allSettled to execute, which will also execute simulataenously and 
  result will be arranged in order👍.

*/

let timeouts = [3000, 2000, 1000, 4000];
let results = [];
const start = Date.now();

// Use array.map to create an array of promises
let promises = timeouts.map((nextTimeout) => {
  return testPromise(nextTimeout);
});

// Use Promise.all to wait for all promises to resolve
Promise.all(promises)
  .then((results) => {logger(results, Date.now() - start);
    console.log("All Promises Resolved !!✨", results);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

/*
  Result output:

Processing 1000
Processing 2000
Processing 3000
Processing 4000
All Promises Resolved !!✨ (4) [3000, 2000, 1000, 4000]
*/ 


/*
  Array forEach: this execute the simultaneously (all starts together).
  This will execute simultaneously and result returned is based on time required for execution (if using Array.push) 
  Array for each definition: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
*/

function testPromise(time) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(`Processing ${time}`);
      resolve(time);
    }, time);
  });
}

let timeouts = [3000, 2000, 1000, 4000];
let results = [];
const start = Date.now();

timeouts.forEach((nextTimeout) => {
  testPromise(nextTimeout)
    .then((result) => {
      logger(result, Date.now() - start);
      results.push(result);
    })
    .catch((error) => {
      console.error(`Error processing ${nextTimeout}:`, error);
    });
});

// For simplicity, I'm logging the results after a delay
setTimeout(() => {
  console.log("All Promises Resolved !!✨", results);
}, Math.max(...ids) + 1000); 

/*
  Result output:

Processing 1000
1000 finished waiting 1 seconds later.
Processing 2000
2000 finished waiting 2 seconds later.
Processing 3000
3000 finished waiting 3 seconds later.
Processing 4000
4000 finished waiting 4 seconds later.
All Promises Resolved !!✨ (4) [1000, 2000, 3000, 4000]
*/ 



/*
  Array Reduce: this execute the async promise one by one. 
  We can derive result by using ".then" since it will have resolved result for each item in array;  
  
  Array reduce definition: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
*/
function testPromise(time) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(`Processing ${time}`);
      resolve(time);
    }, time);
  });
}

let timeouts = [3000, 2000, 1000, 4000];
let results = [];
const start = Date.now();
let resultPromise = timeouts.reduce((accumulatorPromise, nextTimeout) => {
  return accumulatorPromise.then(() => { 
    return testPromise(nextTimeout);
  }).then((result) => { 
    logger(result, Date.now() - start);
    results.push(result);
  });
}, Promise.resolve());

resultPromise.then(() => {
  console.log("All Promises Resolved !!✨", results);
});

/*
>  Result output:
  
Processing 3000
3000 finished waiting 3 seconds later.
Processing 2000
2000 finished waiting 5 seconds later.
Processing 1000
1000 finished waiting 6 seconds later.
Processing 4000
4000 finished waiting 10 seconds later.
All Promises Resolved !!✨ (4) [3000, 2000, 1000, 4000]
*/ 


function logger(value, diffInMS) {
  return console.log(
    `${value} finished waiting ${Math.round(diffInMS / 1000)} seconds later.`
  );
};