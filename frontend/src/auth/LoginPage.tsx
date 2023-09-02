import React, { SyntheticEvent, useState } from 'react'
import { authAPI } from './AuthAPI';

function LoginPage() {
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');

    function isValid() {
      return true;
    }

    const handleSubmit = (event: SyntheticEvent) => {
      event.preventDefault();
      if (!isValid()) return;

      // POST to server
      authAPI.post(username, password)
        .then((resp) => console.log(resp))
        .catch((error) => {console.log(error)})
    }

  return (
    <div>
        <h1>Log Into Your Account</h1>
        <form onSubmit={handleSubmit}>
            <label>Username: </label>
            <input type='text' value={username} onChange={(e) => setUsername(e.target.value)} id='' />
            <br />
            <label>Password: </label>
            <input type='password' value={password} onChange={(e) => setPassword(e.target.value)} id='' />
            <br />
            <button type='submit'>Log In</button>

        </form>
    </div>
  )
}

export default LoginPage