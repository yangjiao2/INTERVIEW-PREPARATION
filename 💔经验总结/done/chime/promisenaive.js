function MyPromise (executor) {
 
    let fullfilled = false;
    let rejected = false;
    let value;
    
    let onResolve = null;
    let onReject = null;
    
    function resolve(v){
      if (!fullfilled) {
        fullfilled = true;
        value = v; // register value
      }
      if (typeof onResolve === 'function'){
        onResolve(value);
      } 
    }
      
    function reject(v){
      if (!rejected) {
        rejected = true;
        value = v; // register value
      }
      if (typeof onReject === 'function'){
        onReject(value);
      }
    }
  
    this.then = function (callback) {
      onResolve = callback;
      if (fullfilled) {
        onResolve(value);
      }
      return this;
    }
  
    this.catch = function (callback) {
      onReject = callback;
      if (rejected) {
          onReject(value);
      }
      return this;
    }
    
    try {
      executor(resolve, reject);
    } catch (err) {
      console.log('error received on promise execution', err);
    }
  }
  
  
  MyPromise.resolve = function (result) {
      return new MyPromise(resolve => {
        resolve(result);
      }
    );
  }
  
  const asyncGetNumber = () => {
    const random = Math.random();
    return new MyPromise((resolve, reject) => {
       setTimeout(() => {
        if (random < 0.5) {
          resolve(random);
        } else {
          reject('Error getting number');
        }
       }, Math.floor(random * 1000));
    });
  };
  
  asyncGetNumber()
      .then(result => {
          console.log(result);
      })
      .catch((e) => {
          console.log('error', e);
      });
  
  const random2 = Math.random();
  const result = MyPromise.resolve(random2); 
  result.then(value => console.log(value));
  