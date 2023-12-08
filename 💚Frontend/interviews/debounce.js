
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


  ----------------


  function debounce(callback, delay) {
    let timeoutId;
    let latestArgs;
  
    function debounced(...args) {
      latestArgs = args;
      clearTimeout(timeoutId);
  
      timeoutId = setTimeout(() => {
        callback(...latestArgs);
        latestArgs = null;
      }, delay);
    }
  
    function cancel() {
      clearTimeout(timeoutId);
      latestArgs = null;
    }
  
    function flush() {
      if (latestArgs) {
        callback(...latestArgs);
        latestArgs = null;
        clearTimeout(timeoutId);
      }
    }
  
    return {
      debounced,
      cancel,
      flush,
    };
  }
  
  // Example usage:
  const debouncedFunction = debounce((value) => {
    console.log(`Debounced function called with value: ${value}`);
  }, 1000);
  
  // Call the debounced function multiple times in quick succession
  debouncedFunction.debounced('A');
  debouncedFunction.debounced('B');
  debouncedFunction.debounced('C');
  
  // After 1500 milliseconds, the debounced function will be called with the last value ('C')
  setTimeout(() => {
    debouncedFunction.debounced('D');
  }, 1500);
  
  // Immediately invoke the debounced function with the latest arguments
  debouncedFunction.flush();
  
  // Cancel the debounced function before it gets a chance to execute
  debouncedFunction.cancel();
  