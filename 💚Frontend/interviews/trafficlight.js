import "./styles.scss";
import * as React from "react";
import { useDeferredValue, useState, useCallback, useEffect } from "react";

export default function App() {
  const [lightIndex, setLightIndex] = useState(0);
  const intervals = [4000, 500, 3000];

  useEffect(() => {
    const timer = setInterval(() => {
      setLightIndex((prevIndex) => (prevIndex + 1) % 3);
    }, intervals[lightIndex]);

    return () => clearInterval(timer);
  }, [lightIndex]);

  return (
    <div>
      {lightIndex} Render your Traffic Light here.
      {["red", "yellow", "green"].map((color, index) => {
        return (
          <div
            key={color}
            style={{
              width: "100px",
              backgroundColor: lightIndex == index ? color : "inherit"
            }}
          >
            {color}
          </div>
        );
      })}
    </div>
  );
}
