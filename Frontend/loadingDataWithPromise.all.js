const useAllData = () => {
    const [sidebar, setSidebar] = useState();
    const [comments, setComments] = useState();
    const [issue, setIssue] = useState();

    useEffect(() => {
        const dataFetch = async () => {
            // waiting for allthethings in parallel
            const result = (
                await Promise.all([
                    fetch(sidebarUrl),
                    fetch(issueUrl),
                    fetch(commentsUrl)
                ])
            ).map((r) => r.json());

            // and waiting a bit more - fetch API is cumbersome
            const [sidebarResult, issueResult, commentsResult] = await Promise.all(
                result
            );

            // when the data is ready, save it to state
            setSidebar(sidebarResult);
            setIssue(issueResult);
            setComments(commentsResult);
        };

        dataFetch();
    }, []);

    return { sidebar, comments, issue };
};

const App = () => {
    // all the fetches were triggered in parallel
    const { sidebar, comments, issue } = useAllData()

    // show loading state while waiting for all the data
    if (!sidebar || !comments || !issue) return 'loading';

    // render the actual app here and pass data from state to children
    return (
        <>
            <Sidebar data={state.sidebar} />
            <Issue comments={state.comments} issue={state.issue} />
        </>
    )
}






// fetch call basically “escapes” all React lifecycle
// and will be fired as soon as javascript is loaded on the page, before any of useEffect anywere are called.
const commentsPromise = fetch('/get-comments');

const Comments = () => {
    useEffect(() => {
        const dataFetch = async () => {
            // just await the variable here
            const data = await (await commentsPromise).json();

            setState(data);
        };

        dataFetch();
    }, [url]);
}

// max:  6 requests in parallel

const Issue = () => {
    return <>
      // issue data
        <Suspense fallback="loading">
            <Comments />
        </Suspense>
    </>
}
