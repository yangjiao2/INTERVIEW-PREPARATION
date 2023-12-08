function throttle(func, limit, interval) {
    let tokens = limit;
  
    return function (...args) {
      if (tokens > 0) {
        tokens--;
        func.apply(this, args);
  
        setTimeout(() => {
          tokens++;
        }, interval);
      } else {
        console.log('Function execution throttled. Try again later.');
      }
    };
  }
  
  // Example usage:
  const obj = {
    value: 'Example',
    logValue(param) {
      console.log(`${this.value} - Function executed with param: ${param}`);
    },
  };
  