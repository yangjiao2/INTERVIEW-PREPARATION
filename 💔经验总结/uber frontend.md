https://leetcode.com/discuss/interview-question/1064199/uber-front-end-phone-screen-reject



https://onecompiler.com/javascript/3z4ts6dkw


// async function load() {
//   const allPromise = Promise.all([
//     resolveTimeout(["potatoes", "tomatoes"], 1000),
//     resolveTimeout(["oranges", "apples"], 1000)
//   ]);

//   // wait...
//   const lists = await allPromise;

//   // after 1 second
//   console.log(lists);
//   // [['potatoes', 'tomatoes'], ['oranges', 'apples']]
// }

// load();

// function resolveTimeout(value, delay) {
//   return new Promise((resolve) => setTimeout(() => resolve(value), delay));
// }

// function rejectTimeout(reason, delay) {
//   return new Promise((r, reject) => setTimeout(() => reject(reason), delay));
// }


// Implement mapLimit, which is a utility function that produces a list of outputs by mapping each input through an asynchronous iteratee function. The provided limit dictates how many operations can occur at once.

// Inputs
// inputs: An array of inputs.
// limit: The maximum number of operations at any one time.
// iterateeFn: The async function that should be called with each input to generate the corresponding output. It will have two arguments:
//      input: The input being processed.
//      callback: A function that will be called when the input is finished processing. It will be provided one argument, the processed output.
// callback: A function that should be called with the array of outputs once all the inputs have been processed.

function getNameById(id, callback) {
  // simulating async request
  const randomRequestTime = Math.floor(Math.random() * 100) + 200;

  setTimeout(() => {
    callback("User " + id);
  }, randomRequestTime);
}

function mapLimit(inputs, limit, iterateeFn, finalCB) {
  const allResults = [];
  let remaining = inputs.length;
  let end = 0;
  
  const eachCallback = (index) => {
    return function (param) {
      allResults[index] = param;
      remaining--;
      if (remaining === 0) {
        finalCB(allResults);
      }
    };
  };

  let i = 0;
  while (i < inputs.length) {
    end = i + limit > inputs.length ? inputs.length : i + limit;
    console.log("-----------");
    while (i < end) {
      console.log(inputs[i]);
      iterateeFn(inputs[i], eachCallback(i));
      i++;
    }
  }
}
mapLimit([1, 2, 3, 4, 5], 2, getNameById, (allResults) => {
  console.log(allResults); // ["User1", "User2", "User3", "User4", "User5"]
});

mapLimit([1, 2, 3, 4, 5], 2, getNameById, (allResults) => {
  console.log("output", allResults); // ["User1", "User2", "User3", "User4", "User5"]
});