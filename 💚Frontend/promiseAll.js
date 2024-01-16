// https://dmitripavlutin.com/promise-all/


let results = []; // to be resolved array of values
// return a promise
return new Promise((resolve, reject) => {
  // checking for [] array
  if (promises.length === 0) {
    resolve([]);
  } else {
    promises.forEach((promise, index) => {
      if (promise instanceof Promise) {
        promise.then((value) => {
          results[index] = value;
          if(results.length === promises.length) {
            // to break the loop
            resolve(results);
          }
        }).catch(function (error) {
          reject(error);
        });
      } else {
        // what if the array value is just a number
        results[index] = promise;
      }
      if(results.length === promises.length) {
        // to break the loop
        resolve(results);
      }
    });
  }
});


Promise.all = function promiseAllIterative(values) {
    return new Promise((resolve, reject) => {
       let results = [];
       let completed = 0;
       
       values.forEach((value, index) => {
            Promise.resolve(value).then(result => {
                results[index] = result;
                completed += 1;
                
                if (completed == values.length) {
                    resolve(results);
                }
            }).catch(err => reject(err));
       });
    });
}


Promise.all = function promiseAllReduce(values) {
    return values.reduce((accumulator, value) => {
        return accumulator.then(results => {
            return Promise.resolve(value).then(result => {
                return [...results, result];
            });
        });
    }, Promise.resolve([]));
}




// all success -> execute array filled with resolved value
// order of array does not matter


//  > 1 reject -> promise reject


function resolveTimeout(value, delay) {
    return new Promise(
        resolve => setTimeout(() => resolve(value), delay)
    );
}
function rejectTimeout(reason, delay) {
    return new Promise(
        (r, reject) => setTimeout(() => reject(reason), delay)
    );
}


const allPromise = Promise.all([
    resolveTimeout(['potatoes', 'tomatoes'], 2000),
    resolveTimeout(['oranges', 'apples'], 1000)
]);
// wait...
const lists = await allPromise;
// after 1 second
console.log(lists);
// [['potatoes', 'tomatoes'], ['oranges', 'apples']]



// https://blog.logrocket.com/understanding-promise-all-in-javascript/

const allpromises1 = Promise.allSettled([first, second, third, fourth, fifth]);
allpromises1.then(success => console.log('success: ', success)).catch(error => console.log('error: ', error));

// -- ALL PASS
// sucess: [ 2, 4, 6, 8, 10 ]
// output all values in array format


// -- ONE FAIL
// failure: error: 11


const allpromises2 = Promise.allSettled([first, second, third, fourth, fifth]);
allpromises2.then(success => console.log('sucess: ', success)).catch(error => console.log('error: ', error));

// Result
// success:  [
//   { status: 'fulfilled', value: 2 },
//   { status: 'fulfilled', value: 4 },
//   { status: 'fulfilled', value: 6 },
//   { status: 'fulfilled', value: 8 },
//   { status: 'rejected', reason: 11 }
// ]


// Async function to send mail to a list of users.
const sendMailForUsers = async (users) => {
    const usersLength = users.length

    for (let i = 0; i < usersLength; i += 100) {
        const requests = users.slice(i, i + 100).map((user) => { // The batch size is 100. We are processing in a set of 100 users.
            return triggerMailForUser(user) // Async function to send the mail.
                .catch(e => console.log(`Error in sending email for ${user} - ${e}`)) // Catch the error if something goes wrong. So that it won't block the loop.
        })

        // requests will have 100 or less pending promises.
        // Promise.all will wait till all the promises got resolves and then take the next 100.
        await Promise.all(requests)
            .catch(e => console.log(`Error in sending email for the batch ${i} - ${e}`)) // Catch the error.
    }
}


sendMailForUsers(userLists)




// ------------

// await /async parallel execution using Promise.all

// -------------------------------------------------------------------
// these functions simulate requests that need to run async
// -------------------------------------------------------------------
function asyncThing1() {
    return new Promise((resolve) => {
        setTimeout(() => resolve('Thing 1 is done!'), 2000);
    });
}

function asyncThing2() {
    return new Promise((resolve) => {
        setTimeout(() => resolve('Thing 2 is done!'), 2000);
    });
}

// -------------------------------------------------------------------
//  NO GOOD
// -------------------------------------------------------------------
// 🚫 don’t do this in your real code; it’s slow!
async function doThings() {
    const thing1 = await asyncThing1();
    console.log(thing1);

    const thing2 = await asyncThing2();
    console.log(thing2);
}

doThings();


// ✅ do this — async code is run in parallel!
async function doThings() {
    const p1 = asyncThing1();
    const p2 = asyncThing2();

    const [thing1, thing2] = await Promise.all([p1, p2]);

    console.log(thing1);
    console.log(thing2);
}

doThings();




// exerise https://codesandbox.io/s/first-fulfilled-forked-5vz7nq


let locArr = [{
    x: 0,
    y: 0
}, {
    x: 2,
    y: 4
}, {
    x: 6,
    y: 8
}];

// my asynchronous function that returns a promise
function findLoc(x, y) {
    return new Promise((resolve, reject) => {
        let a = setTimeout(() => {
            resolve({
                x: x * x,
                y: y * y
            });
        }, 500);
    });
}

Promise.all(
    locArr.map(o => findLoc(o.x, o.y))
).then(values => {
    // all values from all the promises
    console.log(values)
});
