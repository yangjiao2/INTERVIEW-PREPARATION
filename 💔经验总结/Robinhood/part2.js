// ------------ DO NOT EDIT BELOW ------------
import { _initializeStartTime } from "./utils";
import { EventLogger } from "./eventLogger";

function testBatching() {
    _initializeStartTime();

    const eventLogger = new EventLogger(1000);
    eventLogger.logEvent("first-batch-1");
    eventLogger.logEvent("first-batch-2");
    eventLogger.logEvent("first-batch-3");

    setTimeout(() => {
        eventLogger.logEvent("second-batch-1");
    }, 1100);
}

// Expected Results:
// [0ms][LOGGED] first-batch-1
// [0ms][LOGGED] first-batch-2
// [0ms][LOGGED] first-batch-3
// [1000ms][REQUEST START] [first-batch-1, first-batch-2, first-batch-3]
// [~1000ms][REQUEST END] [first-batch-1, first-batch-2, first-batch-3]
// [1100ms][LOGGED] second-batch-1
// [2000ms or 2100ms][REQUEST START] [second-batch-1]
// [~2000ms or ~2100ms][REQUEST END] [second-batch-1]

/* IGNORE BELOW: THEY ARE FOR BUTTON SETUP */
if (!document.getElementById("test-button")) {
    const btn = document.createElement("button");
    btn.id = "test-button";
    btn.innerText = "Run Tests for Part 2";
    btn.addEventListener("click", () => {
        testBatching();
    });
    document.body.appendChild(btn);
}
