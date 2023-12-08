const list = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10];
 
export async function mainWithFor() {
  const start = Date.now();
  const logger = getLogger("mainWithFor");
  for (const item of list) {
    await waitFor(2);
    const later = Date.now();
    logger(item, later - start);
  }
}

// 0, 2, 4, 6 ..

// `for loop`
// execute each loop until previous loop conmpletely finish



export async function mainWithForEach() {
    const start = Date.now();
    const logger = getLogger("mainWithForEach");
    list.forEach(async (item) => {
      await waitFor(2);
      const later = Date.now();
      logger(item, later - start);
    });
  }
 
  

  export async function mainWithMap() {
    const start = Date.now();
    const logger = getLogger("mainWithMap");
    const promises = list.map(async (item) => {
      await waitFor(2);
      const later = Date.now();
      logger(item, later - start);
    });
    const finalAnswer = await Promise.all(promises)
  }

// both `forEach` and `map` run callbacks start at the same time
// `map` returns an array of promises,


// NEVER call async-await functions inside a forEach loop.


for (const [book, price] of Object.entries(books)) {
    if (price === 0) {
      console.log(book);
    }
  }