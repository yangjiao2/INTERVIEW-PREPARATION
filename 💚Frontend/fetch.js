useEffect(() => {
    let cancelRequest = false;
    if (!url) return;

    const fetchData = async () => {
        dispatch({ type: 'FETCHING' });
        if (cache.current[url]) {
            const data = cache.current[url];
            dispatch({ type: 'FETCHED', payload: data });
        } else {
            try {
                const response = await fetch(url);
                const data = await response.json();
                cache.current[url] = data;
                if (cancelRequest) return;
                dispatch({ type: 'FETCHED', payload: data });
            } catch (error) {
                if (cancelRequest) return;
                dispatch({ type: 'FETCH_ERROR', payload: error.message });
            }
        }
    };

    fetchData();

    return function cleanup() {
        cancelRequest = true;
    };
}, [url]);






const login = async event => {
    event.preventDefault();
    const response = await fetch("/api", {
        method: "POST",
        body: JSON.stringify({
            username,
            password,
        }),
    });
    // Here we could check response.status to login or show error
};



//   fetch() API by itself doesn't allow canceling programmatically a request. To stop a request at the desired time you need additionally an abort controller.

The following fetchWithTimeout() is an improved version of fetch() that creates requests with a configurable timeout:

async function fetchWithTimeout(resource, options = {}) {
    const { timeout = 8000 } = options;

    const controller = new AbortController();
    const id = setTimeout(() => controller.abort(), timeout);
    const response = await fetch(resource, {
        ...options,
        signal: controller.signal
    });
    clearTimeout(id);
    return response;
}


useEffect(() => {
    let abortController = new AbortController();
    const fetchData = async () => {
        try {
            const response = await fetch(endpoint, {
                ...options,
                signal: abortController.signal,
            });
            const newData = await response.json();
            setIsLoading(false);
            setFetchedData(newData);
        } catch (error) {
            if (error.name === "AbortError") {
                setError(error);
                setIsLoading(false);
            }
        }
    };
    fetchData();
    return () => {
        abortController.abort();
    };
}, [endpoint, options]);
