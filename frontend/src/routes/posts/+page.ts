export const load = async ({ setHeaders }) => {
	const res = await fetch('http://127.0.0.1:8000/api/posts');
	const posts = await res.json();

	setHeaders({
		'Access-Control-Allow-Origin': '*'
	});

	return {
		posts
	};
};
