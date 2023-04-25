
//  debouncing calls the function after the user has completed typing
//  throttled function is called every n milliseconds, limiting how many times a function is called.

// https://codesandbox.io/s/quizzical-sun-qdv7p?from-embed

window.addEventListener('scroll', throttle(callback, 1000));

function throttle(fn, wait) {
  var time = Date.now();
  return function () {
    if ((time + wait - Date.now()) < 0) {
      fn();
      time = Date.now();
    }
  }
}

const throttle = (fn, wait) => {
  let inThrottle, lastFn, lastTime;
  return function () {
    const context = this,
      args = arguments;
    if (!inThrottle) {
      fn.apply(context, args);
      lastTime = Date.now();
      inThrottle = true;
    } else {
      clearTimeout(lastFn);
      lastFn = setTimeout(function () {
        if (Date.now() - lastTime >= wait) {
          fn.apply(context, args);
          lastTime = Date.now();
        }
      }, Math.max(wait - (Date.now() - lastTime), 0));
    }
  };
};


function throttle(fn, delay) {
  let previous = 0;
  let timer = null;

  return function () {
    let _this = this;
    if (new Date() - previous > delay) {
      clearTimeout(timer);
      timer = null;
      fn.apply(this, args)
      previous = new Date();
    } else {
      timer = setTimeout(() => {
        fn.apply(_this, args), delay
      })
    }
  }

}



function throttle(func, wait) {
  let waiting = false;
  return function () {
    if (waiting) {
      return;
    }

    waiting = true;
    setTimeout(() => {
      func.apply(this, arguments);
      waiting = false;
    }, wait);
  };
}


const onScroll = throttle(() => {
  // do something
}, 100);

document.addEventListener('scroll', onScroll)

// ---------


const useThrottledEffect = (callback, delay, deps = []) => {
  const lastRan = useRef(Date.now());

  useEffect(() => {
    const handler = setTimeout(function () {
      if (Date.now() - lastRan.current >= delay) {
        callback();
        lastRan.current = Date.now();
      }
    }, delay - (Date.now() - lastRan.current));

    return () => {
      clearTimeout(handler);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [delay, ...deps]);
};



----

import React from "react";
import { useEffect, useState } from "react";
import { ProfileCard, ProfileLoadingCard } from "./components/card";
import "./app.scss";
import { apiCall } from "./api";
import { useInfiniteScroll } from "./customHooks";

function App() {
  const [nextPage, setNextPage] = useState(null);
  const [APIError, SetAPIError] = useState(null);
  const [data, setData] = useState(null);
  const [isFetching, setIsFetching, stop] = useInfiniteScroll(getMoreFeed);

  async function getMoreFeed() {
    if (nextPage) {
      const res = await apiCall({ method: "GET", page: nextPage });
      if (res === 500) {
        SetAPIError(500);
      } else {
        setData([...data, ...res.data]);
        setIsFetching(false);
        res.next
          ? setNextPage(nextPage + 1)
          : setNextPage(null)((stop.current = true));
      }
    } else {
      setIsFetching(false);
    }
  }

  useEffect(() => {
    const getFeed = async () => {
      const res = await apiCall({ method: "GET" });
      if (res === 500) {
        SetAPIError(500);
      } else {
        setData(res.data);
        res.next ? setNextPage(2) : setNextPage(null)((stop.current = true));
      }
    };

    getFeed();
  }, []);

  if (APIError === 500) {
    return <h1>Some error occured</h1>;
  } else {
    return (
      <div className="feed_container">
        {!data && <ProfileLoadingCard />}
        {data?.map((profile) => {
          return (
            <ProfileCard
              key={profile.id}
              avatar={profile.avatar}
              firstName={profile.first_name}
              lastName={profile.last_name}
            />
          );
        })}

        {isFetching && nextPage && <ProfileLoadingCard number={5} />}
        {!nextPage && <h4>..... you have reached end of the feed .....</h4>}
      </div>
    );
  }
}

export default App;


---
