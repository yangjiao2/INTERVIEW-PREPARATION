// debounced function will only run ONCE after a certain delay since the last time it was triggered.

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
