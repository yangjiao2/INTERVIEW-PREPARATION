import { eventLogger } from "./eventLogger";

// TODO: Implement for Part 1
// Goal:
// When clicking on the colored square, we should send
// the following payload through network request:
// {
//   "events": [{
//     "eventName": "click",
//     "hostname": "1ic4u.csb.app", // Hostname of the current page
//     "timestamp": "2021-04-06T00:33:42.304Z", // Current UTC time in ISOString format
//     "data": {
//        "color": "rgb(255, 80, 0)" // Background color of the square
//     }
//   }]
// }

let grids = document.getElementsByClassName("square");
// console.log(grids);

for (let i = 0; i < grids.length; i++) {
    grids[i].addEventListener("click", (e) => {
        eventLogger.logEvent("click", {
            events: [
                {
                    eventName: "click",
                    hostname: window.location.href.slice(8, -1), // Hostname of the current page
                    timestamp: new Date(Date.now()).toISOString(), // Current UTC time in ISOString format
                    data: {
                        color: window.getComputedStyle(grids[i]).color // Background color of the square
                    }
                }
            ]
        });
    });
}
