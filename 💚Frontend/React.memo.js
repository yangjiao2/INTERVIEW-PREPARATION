import * as React from 'react';

type AProps = React.PropsWithChildren<{
  a: string;
}>;

/* 
Will re-render only if a prop changes or if it has a children prop and 
its parent renders.

Children is special though, because when the state of a component
that has children updates, if its children are the
same, then it wont rerender.

"If a React component returns the exact same element reference in its 
render output as it did the last time, React will skip re-rendering 
that particular child."
*/
export const A = React.memo(({ children, a }: AProps) => {
  const counter = React.useRef(0);
  console.log('memo A rendered', counter.current++);

  return <div style={{backgroundColor: 'orange', padding: 8}}>
    {children}
  </div>
});
