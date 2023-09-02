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
            <p>You are not logged in</p>
            <div>
                <a href='/login' style={{'padding': '5px'}}>Login</a>
                <a href='/register'>Register</a>
            </div>
        </div>
    )
}

export default HomePage;