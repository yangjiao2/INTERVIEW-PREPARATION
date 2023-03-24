import { sendRequest, _logToConsole, _setFetchResponseDelay } from "./utils";

/**
 * `sendRequest` is a helper function to send your request with
 * following type signature:
 *
 * sendRequest(body: Object) => Promise<void>
 *
 * You can abort the request "in-flight" via the following:
 *
 * const requestPromise = sendRequest()
 * requestPromise.abort()
 *
 */

// Sample Event Payload
// {
//   "events": [{
//     "eventName": "click",
//     "hostname": "1ic4u.csb.app", // Hostname of the current page
//     "timestamp": "2021-04-06T00:33:42.304Z", // Current UTC time in ISOString format
//     "data": {}
//   }]
// }

export class EventLogger {
    constructor(time) {
        this.time = time;
        this.queue = [];
        // console.log("time", this.time);
    }

    logEvent(eventName, data) {
        // DO NOT REMOVE -- This is for testing your output
        _logToConsole(`[LOGGED] ${eventName}`);
        this.queue.push(eventName);
        if (this.queue.length === 1) {
            setTimeout(() => {
                sendRequest(this.queue);
                this.queue = [];
            }, this.time);
        }
    }
}

const eventLogger = new EventLogger();
export { eventLogger };
