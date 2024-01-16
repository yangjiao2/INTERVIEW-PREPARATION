// Properties:
// AbortController.signal:
// Returns an AbortSignal object instance, which can be used to communicate with, or to abort, a DOM request.

// Method:
// AbortController.abort():
// Aborts a DOM request before it has been completed. When we abort an async operation, the promise rejects with a DOMException named AbortError.





const url = 'https://google.com'
const controller = new AbortController()

await fetch(url, {
  signal: controller.signal
})

setTimeout(() => {
  controller.abort()
}, 1000)



<script setup lang="ts">
  let controller

  const onCancel = () => {
    controller?.abort()
  }

  const onClick = async () => {
    controller = new AbortController()
    await fetch(url, { signal: controller.signal })
  }
</script>

///
// Let's take a look at the fetch() function.

fetch(url)
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));


<!DOCTYPE html>
<html>
  <body>
    <input id="search" type="number" />
    <script>
      const results = [];
      const search = document.getElementById("search");
      let controller = new AbortController();
      let signal = controller.signal;

      const getPost = async (value, signal) => {
        try {
          const response = await fetch(
            `https://jsonplaceholder.typicode.com/posts/${value}`,
            { signal }
          );
          results.push(`Success: ${value}`);
        } catch (error) {
          if (error.name === "AbortError") {
            results.push("API failure");
          } else {
            console.log("Some other error");
          }
        } finally {
          console.log("Status", results);
        }
      };
      const onChange = () => {
        const value = search.value;
        if (value) {
          controller.abort();
          controller = new AbortController();
          signal = controller.signal;
          getPost(value, signal);
        }
      };
      search.onkeyup = onChange;
    </script>
  </body>
</html>


import React, { useEffect, useState } from 'react';

export default function DataDisplayer(props) {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`https://swapi.dev/api/people/${props.id}/`);
      const newData = await response.json();
      setData(newData);
    };

    fetchData();
  }, [props.id]);

  if (data) {
    return <div>{data.name}</div>;
  } else {
    return null;
  }
}



useEffect(() => {
    const controller = new AbortController();
    const signal = controller.signal;
    const results = [];
    const getPost = async (value) => {
      try {
        const response = await fetch(
          `https://jsonplaceholder.typicode.com/posts/${value}`,
          { signal }
        );
        results.push(`Success: ${value}`);
      } catch (error) {
        if (error.name === "AbortError") {
          results.push("API failure");
        }
      } finally {
        console.log("Status", results);
      }
    };

    getPost(1);

    return () => {
      // Cancel the request on unmount
      controller.abort();
    };
  }, []);
