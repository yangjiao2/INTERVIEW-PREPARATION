
// https://blog.logrocket.com/react-hooks-cheat-sheet-unlock-solutions-to-common-problems-af4caf699e70/


const [count, setCount] = useState(0);


useEffect
useEffect(
    () => {
      setEffectLogs(prevEffectLogs => [...prevEffectLogs, 'effect fn has been invoked'])
    },
    [number]
  )
will be called on mount and whenever a new random number is generated.


```
useEffect(
    () => {
      setEffectLogs(prevEffectLogs => [...prevEffectLogs, 'effect fn has been invoked'])
    },
    []
  )

```

useEffect is passed an empty array, []
called only on mount.


context:  handling shared data between multiple components.
const ThemeContext = React.createContext("dark");

```
import {useContext} from 'react';

function ButtonHooks() {
 const theme = useContext(ThemeContext)
 return <button className={theme}>Amazing button</button>
}

```

useEffect fires after layout and paint
— i.e., after the render has been committed to the screen.
- not ideal for " a visual change to the DOM as a side effect "


useLayoutEffect will be
run before the browser updates the screen.
- prevent the user from seeing flickers of changes
```
useLayoutEffect(() => {
//do something
}, [arrayDependency])
```

useRef: Accessing the DOM

```
const textAreaEl = useRef(null);

const handleBtnClick = () => {
    textAreaEl.current.value =
    "The is the story of your life. You are an human being, and you're on a website about React Hooks";
    textAreaEl.current.focus();
  };


<textarea ref={textAreaEl} id="story" rows="5" cols="33" />
```


```
function TimerWithRefID() {
    const setIntervalRef = useRef();

    useEffect(() => {
      const intervalID = setInterval(() => {
        // something to be done every 100ms
      }, 100);

      // this is where the interval ID is saved in the ref object
      setIntervalRef.current = intervalID;
      return () => {
        clearInterval(setIntervalRef.current);
      };
    });
  }

```


```
const [data, setData] = useState(initialData)

const [gender, setGender] = useState('female')
const [loading, setLoading] = useState(false)

useEffect(
  () => {
    const fetchData = () => {
      setLoading(true)
      const uri = 'https://randomuser.me/api/?gender=' + gender
      fetch(uri)
        .then(res => res.json())
        .then(({ results }) => {
          setLoading(false)
          const { name, gender, dob } = results[0]
          const dataVal = stringifyData({
            ...name,
            gender,
            age: dob.age
          })
          setData(dataVal)
        })
    }

    fetchData()
  },
  [gender]
)


```

no callback or re-render when a component is (un)mounted and attached to ref.current using useRef.
when
useRef to get a reference to it and useEffect to respond to its mounts and unmounts
when


Mutable values like imageRef.current is not valid dependencies
since mutating ref.current will not re-render
like:
```
useEffect(() => {
    setInfo(imageRef.current?.backgroundColor)
}, [imageRef, imageRef.current])
```



// https://codesandbox.io/s/how-useref-and-useeffect-cant-track-a-nodes-render-27br6?from-embed
