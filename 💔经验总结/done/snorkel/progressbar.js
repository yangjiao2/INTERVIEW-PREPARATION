import "./styles.css";
import { useState, useEffect, useRef } from "react";

// progress bar
// fill 10 sec, then restart
export default function App() {
  const [count, setCount] = useState(1);
  const [counter, setCounter] = useState(1);
  const counterRef = useRef(1);

  return (
    <div>
      <p> CounterRef: {counterRef.current} </p>
      <p> Counter: {counter}</p>
      <button onClick={() => setCount((prev) => prev + 1)}> Add </button>
      {[...Array(count).keys()].map((ele) => {
        return (
          <ProgressBar
            key={ele}
            counterRef={counterRef}
            updateCounter={() => setCounter((prev) => prev + 1)}
          />
        );
      })}
    </div>
  );
}

function ProgressBar({ counterRef, updateCounter }) {
  const [progress, setProgress] = useState(0);
  // USE ENUM
  // status = 0, stop; status = 1, start;
  const [status, setStatus] = useState(0);

  useEffect(() => {
    const updateProgress = () => {
      setProgress((prev) => {
        if (prev == 10) {
          return 0;
        }
        return prev + 1;
      });
    };

    let intervalId;
    if (status == 1) {
      intervalId = setInterval(updateProgress, 1000);
    }

    return () => {
      clearInterval(intervalId);
    };
  }, [status]);

  useEffect(() => {
    if (progress == 10) {
      updateCounter();
      counterRef.current += 1;
    }
  }, [progress, counterRef]);
  return (
    <div className="container">
      progress bar
      <div className="progressBar" style={{ width: `${progress * 10}%` }}></div>
      <button
        onClick={() => {
          setStatus(1);
        }}
      >
        start
      </button>
      <button
        onClick={() => {
          setStatus(0);
        }}
      >
        stop
      </button>
    </div>
  );
}


```


import { useState, useRef } from 'react';

export default function Chat() {
  const [text, setText] = useState('');
  const [isSending, setIsSending] = useState(false);
  const timeoutRef = useRef(null);

  function handleSend() {
    setIsSending(true);
    timeoutRef.current = setTimeout(() => {
      alert('Sent!');
      setIsSending(false);
    }, 3000);
  }

  function handleUndo() {
    setIsSending(false);
    clearTimeout(timeoutRef.current);
  }

  return (
    <>
      <input
        disabled={isSending}
        value={text}
        onChange={e => setText(e.target.value)}
      />
      <button
        disabled={isSending}
        onClick={handleSend}>
        {isSending ? 'Sending...' : 'Send'}
      </button>
      {isSending &&
        <button onClick={handleUndo}>
          Undo
        </button>
      }
    </>
  );
}


import { useState, useRef } from 'react';

export default function Chat() {
  const [text, setText] = useState('');
  const textRef = useRef(text);

  function handleChange(e) {
    setText(e.target.value);
    textRef.current = e.target.value;
  }

  function handleSend() {
    setTimeout(() => {
      alert('Sending: ' + textRef.current);
    }, 3000);
  }

```