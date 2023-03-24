// throttle

const data = Array(200).fill('');
const concurrent = 20;
let requests = 0;
const start = new Date();

(async () => {

  while (data.length) {

    // Batched concurret request per second
    await new Promise((resolve) => setTimeout(resolve, 1000));
    const batch = data.splice(0, concurrent).map(API);
    const results = await Promise.allSettled(batch);

    // For testing
    const timeTotal = Math.round((requests / (new Date() - start)) * 1000);
    console.log(`Requests per second (total): ${timeTotal}/${data.length}`);

    // Deal with errors
    for (const { status, reason } of results) {
      if (status === 'rejected') {
        console.error(`There was an error ${reason}`);
      }
    }
  }
})()

async function API() {
  requests++;
  await new Promise((resolve) => setTimeout(resolve, 0));
}

/******************
 * IMPLEMENTATION *
 ******************/

/*
 * mapLimit has the following signature:
 * @param {Array} inputs - The list of inputs
 * @param {number} limit - The maximum number of requests
                           that can be handled at once
 * @param {AsyncFunc} iteratee - The async function to be called
 * @param {Function} finalCallback - Called with the list of results,
                                     in the same order as the inputs,
                                     when all requests have finished
 *
 * AsyncFunc has the following signature:
 * @param {*} input - A single input from the list
 * @param {Function} callback - Called with the result of the async request
 */
async function mapLimit(inputs, limit, iteratee, finalCallback) {
  // Implement here

  // iteratee(inputs[0])
  // iteratee(inputs[1])


  let args = [];
  let ptr = 0
  let vals = [];
  async function checkValid(ptr) {
    if (args.length == 0) {
      args = inputs.slice(ptr, ptr + limit);
      if (ptr > inputs.length) {
        console.log(vals);
        finalCallback(vals);
        return;
      }
      checkValid(ptr);
    } else {
      // console.log(vals);
      let p = [];
      for (let i = 0; i < args.length; i++) {
        p.push('User' + args.at(i));
      }
      const promiseAll = Promise.all(
        args.slice(ptr, ptr + limit).map(value => iteratee(value, (v) => {
          console.log('sss', v);
          return p.push(v);
          // vals = vals.concat(v);
        }))
      );

      // promiseAll.then(
      //     value => {
      //         iteratee(value, finalCallback)
      //     }
      // );
      await promiseAll;
      // promiseAll.then(
      //     value => {
      //       console.log('values', value);
      //        vals = vals.concat(value);
      //     }
      // );
      args = [];
      checkValid(ptr + limit);
    }

  }

  // for (let i = 0; i< inputs.length; i++){
  //       iteratee([inputs.at(inputs[i])], finalCallback);
  // }

  return checkValid(ptr);

}

/*****************
* EXAMPLE USAGE *
*****************/

// Expected output: [ 'User1', 'User2', 'User3', 'User4', 'User5' ]
mapLimit([1, 2, 3, 4, 5], 2, getNameById, results => {
  console.log(results)
})

// Simulates an async request
function getNameById(id, callback) {
  const timeout = 100 + Math.random() * 200
  setTimeout(() => {
    callback('User' + String(id));
  }, timeout)
}
