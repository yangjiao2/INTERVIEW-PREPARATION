// program to display time every 3 seconds
function showTime() {

    // return new date and time
    let dateTime = new Date();

    // returns the current local time
    let time = dateTime.toLocaleTimeString();

    console.log(time)

    // display the time after 3 seconds
    setTimeout(showTime, 3000);
}

// calling the function
showTime();


// program to expotentially delay on timeout


let delay = 5000;

let timerId = setTimeout(function request() {
  ...send request...

  if (request failed due to server overload) {
    // increase the interval to the next run
    delay *= 2;
  }

  timerId = setTimeout(request, delay);

}, delay);