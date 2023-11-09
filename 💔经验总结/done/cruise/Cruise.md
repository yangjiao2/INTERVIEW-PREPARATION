whatsapp的聊‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌天系统



import React, {useState, useEffect} from 'react'
import './App.css'

const colors = ['blue', 'red', 'green', 'yellow', 'orange', 'brown', 'pink', 'navy'];
const range = (max) => Math.floor(Math.random() * max);
// A LightController is an EventEmitter which emits a 'message' event.
// The message event has a color field as a string
// and an index field as a number between 0 - 63.
class Lights {
  removeCount = 0;
  listeners = {};
  constructor() {
    setInterval(() => (this.removeCount = 0), 1000);
    setInterval(() => {
      const color = colors[range(colors.length)]; // integer
      const index = range(64);
      // console.log('setInterval');
      (this.listeners["message"] || []).forEach(cb => cb({ color, index }));
    }, 100);
  }
  addEventListener(action, callback) {
    this.listeners[action] = this.listeners[action] || [];
    if (this.listeners[action].length > 10) {
      throw new Error('Too many listeners added...something is wrong');
    }
    this.listeners[action].push(callback)
  }
  removeEventListener(action, callback) {
    if (this.removeCount++ > 10) {
      throw new Error('Too many listeners removed...something is wrong');
    }
    this.listeners[action] = this.listeners[action].filter(cb => cb !== callback);
  }
}


let i = 0;
let grids = []
for (let i = 0; i < 64; i++ ){
  grids.push( colors[(range(i) % colors.length)]);
}

const lights = new Lights();
function App() {
 
  // const grid = <div style={"backgroundColor": "blue"}> </div>;
  // return <div>

  const [gridcolor, setGridColor] = useState(grids);
  
  const createGrid = (color) => {
    return <div  style={{backgroundColor: color, width: "40px", height: "40px"}}> </div>
  }

  console.log(gridcolor);
  // const cells = ;
  useEffect( () => {
    lights.addEventListener('message', ({color, index}) => {

      setGridColor(prevGc => {
        let newGc = [...prevGc];
        newGc[index] = color;
        return newGc;
      });
  
      // return lights.removeEventListener()
    });
  }, [] );
  
 
  return <div class="container">{gridcolor.map(gc => createGrid(gc))}</div>;
  // return <img src="https://user-images.githubusercontent.com/50081/55971375-f8042c80-5c46-11e9-9581-628c7753a4d9.png" />;
}

export default App
