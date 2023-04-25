import React, { useRef, useEffect } from 'react';

const MyListComponent = () => {
  const listInnerRef = useRef();

  const onScroll = () => {
    if (listInnerRef.current) {
      const { scrollTop, scrollHeight, clientHeight } = listInnerRef.current;
      if (scrollTop + clientHeight === scrollHeight) {
        // TO SOMETHING HERE
        console.log('Reached bottom')
      }
    }
  };

  return (
    <div className="list">
      <div className="list-inner" onScroll={() => onScroll()} ref={listInnerRef}>
        {/* List items */}
      </div>
    </div>
  );
};

export default List;
