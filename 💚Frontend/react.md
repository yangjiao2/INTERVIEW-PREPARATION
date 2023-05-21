https://andreassujono.medium.com/ace-your-next-react-interview-9227fc8ca105

* React:
heuristic approach to compare virtual and real DOM during  Reconciliation. Reconciliation is a process of comparing React virtual DOM with the real DOM.

* ShadowDOM:
ShadowDOM is another copy of DOM that is used for localization and isolation. scope of the variables per module is declared and it also helps to localize CSS or scoped CSS

* hooks

useEffect: acts on 3 component lifecycle: componentDidMount, componentDidUpdate, and componentWillUnmount

context: store static data such as app themes, user data, etc

useMemo: memoizes the value returned

useRef: store any dynamic data that don’t want to cause any rerendering

forwardRef: parent wants to access data or invoke a function in the child component.

* Code splitting:
split the code into multiple chunks and load it lazily.

* Tree shaking: split the application into separate multiple chunks during the bundling process.

* React: a client-side rendering, return a blank HTML template

pro: faster
cons: device capacity

* key: should not be index => avoid rerender on insert
