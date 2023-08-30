import { useEffect, useState } from "react";

function HomePage() {
    const [didMount, setDidMount] = useState(false);
    
    useEffect(() => {
        setTimeout(() => {
            setDidMount(true);
        }, 2000)
    }, [])

    return (
        <div>
            {didMount ? (
                <div> Did mount </div>
            ) : (
                <div> Mounting </div>
            )}
        </div>
    )
}

export default HomePage;