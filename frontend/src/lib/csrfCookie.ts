export async function getCsrfToken() {
	const server_url = 'http://localhost:8000'; // Replace with your Django backend URL
	const response = await fetch(server_url + '/csrf-token/', {
		credentials: 'include'
	});

	const data = await response.json();
	const csrfToken = data.csrfToken;

	console.log('CSRF token response:', data);
	console.log('CSRF token for request:', csrfToken);

	return csrfToken;
}
