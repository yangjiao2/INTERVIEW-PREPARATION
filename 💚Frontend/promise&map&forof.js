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


const arr = [1, 2, 3, 4, 5, 6, 7, 8];
const randomDelay = () => new Promise(resolve => setTimeout(resolve, Math.random() * 1000));

const calc = async n => {
  await randomDelay(); 
  console.log('n', n); // out of order
  return n * 2;
};

const asyncFunc = async () => {
  const p = arr.map(n => calc(n));
  const results = await Promise.all(p);
  console.log(results);
};

asyncFunc();
[2,4,6,8,10,12,14,16]



const fruitsToGet = ['apple', 'grape', 'pear']

const mapLoop = async () => {
  console.log('Start')

  const promises = await fruitsToGet.map(async fruit => {
    const numFruit = new Promise((resolve, reject) => {
      setTimeout(() => resolve(fruit), math.random() * 1000)
    });
    return numFruit
  })
  const numFruits = await Promise.all(promises)
  console.log(numFruits)

  console.log('End')
}

mapLoop(); // ["apple","grape","pear"]



const forOfLoop = async () => {
  console.log('Start ')

  let promises = [];
  for (const fruit of fruitsToGet) {
    promises.push(new Promise((resolve, reject) => {
      setTimeout(() => resolve(fruit), Math.random() * 1000)
    }));
  }
  const numFruits = await Promise.all(promises)
  console.log(numFruits)

  console.log('End ')
}

forOfLoop();





const emails = ['alice@gmail.com', 'bob@gmail.com', 'charlie@gmail.com'];
const send = email =>
  new Promise(resolve =>
    setTimeout(() => resolve(email), 1000)
  );
const sendAllEmails = async () => {
  for (email of emails) {
    const emailInfo = await send(email);
    console.log(`Mail sent to ${emailInfo}`);
  }
  console.log('All emails were sent');
};
sendAllEmails();