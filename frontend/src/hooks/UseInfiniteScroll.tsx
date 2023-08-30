import { useEffect, useState } from "react";

const useInfiniteScroll = (callback: () => void) => {
    const [isFetching, setIsFetching] = useState(false);
    
    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, [])

    useEffect(() => {
        if (!isFetching) return;
        callback();
    }, [isFetching])

    function handleScroll() {
        if (window.innerHeight + document.documentElement.scrollTop !== document.documentElement.scrollHeight) return;
        setIsFetching(true);
    }

    return [isFetching, setIsFetching] as const;
}

export default useInfiniteScroll;