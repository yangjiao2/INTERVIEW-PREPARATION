// debounced function will only run ONCE after a certain delay since the last time it was triggered.

import { useCallback } from "react"

// group multiple triggers into one trigger

// example: autocomplete, infinite scroll


function debounce(cb, delay = 250) {
  let timeout

  return (...args) => {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      cb(...args)
    }, delay)
  }
}




const updateOptions = debounce(query => {
  fetch(`/api/getOptions?query=${query}`)
    .then(res => res.json())
    .then(data => setOptions(data))
}, 1000)

input.addEventListener("input", e => {
  updateOptions(e.target.value)
  )}




function debounce(func, wait) {
  let timeout;
  return () => {
    if (timeout) {
      clearTimeout(timeout);
    }
    timeout = setTimeout(func, wait)
  }
}

const onType = debounce(() => {
  // send request
}, 500);

const searchField = document.querySelector('#searchField')
searchField.addEventListener('keydown', onType)


// 防抖函数执行回调等待时间大于等于x；节流函数执行回调等待时间始终为x；
// 防抖函数适用场景：搜索框搜索输入并请求数据、resize；节流函数适用场景：scorll、mousedown

function debounce(cb, delay = 250) {
  let timeout

  return (...args) => {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      cb(...args)
    }, delay)
  }
}

function debounce2(callback, delay) {
  let timer = null;
  var that = this;

  return function () {
    var args = Array.prototype.slice.call(arguments);

    if (timer !== null) {
      clearTimeout(timer)
    }

    timer = setTimeout(() => {
      callback.apply(that, args)
    }, delay)
  }
}

function debounce3(callback, delay = 1000) {
  var time;

  return (...args) => {
    clearTimeout(time);
    time = setTimeout(() => {
      callback(...args);
    }, delay);
  };
}

// wait till 250, 1nd time call

const getSearchResult = throttle(() => {
  numberOfApiCalls += 1;
  console.log('Number of API Calls : ' + numberOfApiCalls);
}, 1000);

searchBarDom.addEventListener('input', function (e) {
  numberOfKeyPresses += 1;
  console.log('Search Keyword : ' + e.target.value);
  console.log('Number of Key Presses : ' + numberOfKeyPresses);
  getSearchResult();
});


function throttle(cb, delay = 250) {
  let shouldWait = false

  return (...args) => {
    if (shouldWait) return

    cb(...args)
    shouldWait = true
    setTimeout(() => {
      shouldWait = false
    }, delay)
  }
}

function throttle(fn, delay) {
  var timer = null;
  var that = this;

  return function () {
    var args = Array.prototype.slice.call(arguments);

    if (!timer) {
      timer = setTimeout(() => {
        fn.apply(that, args);
        timer = null;
      }, delay)
    }
  }
}

// 1st time call, wait till 250, 2nd time call




function throttle(callback, delay = 1000) {
  let shouldWait = false;

  return (...args) => {
    if (shouldWait) return;

    callback(...args);
    shouldWait = true;
    setTimeout(() => {
      shouldWait = false;
    }, delay);
  };
}
