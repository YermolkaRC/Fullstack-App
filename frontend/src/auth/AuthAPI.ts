const baseUrl = 'http://localhost:5000';
const url = `${baseUrl}/auth`;

function translateStatusToErrorMessage(status: number) {
    switch (status) {
        case 401:
            return 'Invalid username or password';
        case 403:
            return 'You do not have permission to view the project(s)';
        default:
            return 'Unexpected error';
    }
}

function checkStatus(response: any) {
    if (response.ok) {
        return response;
    } else {
        const httpErrorInfo = {
            status: response.status,
            statusText: response.statusText,
            url: response.url,
        };
        console.log(`LOG server http error: ${JSON.stringify(httpErrorInfo)}`);

        let errorMessage = translateStatusToErrorMessage(httpErrorInfo.status);
    }
}

function parseJSON(response: Response) {
    return response.json();
}

const authAPI = {
    post(username: string, password: string) {
        return fetch(`${url}/login`, {
            method: 'POST',
            body: JSON.stringify({username: username, password: password}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(checkStatus)
            .then(parseJSON)
            .catch((error: TypeError) => {
                console.log('LOG client error ' + error);
                throw new Error(
                    'There was an error in auth POST'
                    )
            })
    }
}

export { authAPI }