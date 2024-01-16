import './App.css';
import React, { useState, useEffect } from 'react';

// Loading Bar (0-100% over some arbitrary amount of time)
// [======    ]
// Pause/Resume/Reset (buttons)

const _setInterval = () => {}

const App = () => {

    const [percentage, setPercentage] = useState(0);
    // PAUSE, RESUME, RESET
    // const [status, setStatus] = useState('PAUSE');
    const [pause, setPause] = useState(false);
    
    useEffect(() => {
        let interval;

        const increase = () => {
            if (!pause) {
                setPercentage(prev => {
                    if (prev < 100) {
                        return prev += 1;
                    }
                    return prev;
                });
            }
        }

        interval = setInterval(increase, 100);

        return () => {
            clearInterval(interval);
        }
    }, [pause]);

    const handlePause = () => {
        // setStatus('PAUSE');
        setPause(true);
    }

    const handleResume = () => {
        // setStatus('PAUSE');
        setPause(false);
    }

    const handleReset = () => {
        // setStatus('PAUSE');
        setPause(false);
        setPercentage(0);
    }

    return (
        <div className="App">
            Loading Bar {percentage}
            <div style={{ 
                height: '10px', 
                width: `${percentage}%`, backgroundColor: 'green' }}> 
            </div>

            <div>
                <button onClick={handlePause} disabled={pause}>  PAUSE </button>
                <button onClick={handleResume} disabled={!pause} >  RESUME </button>            
                <button onClick={handleReset} >  RESET </button>
            </div>
        </div>
    );
}

const Button = () => {

}

{/* 

const Pausebutton;

<LoadingBar buttonComponent={Pausebutton} etc...>
<LoadingBar buttonComponent={Pausebutton}>
<LoadingBar buttonComponent={Pausebutton}>
<LoadingBar buttonComponent={Pausebutton}>
<LoadingBar buttonComponent={Pausebutton}>



*/}

const LoadingBar = ({buttonComponent: Button}) => {
    return null; // Returns your loading bar
}

export default App;
