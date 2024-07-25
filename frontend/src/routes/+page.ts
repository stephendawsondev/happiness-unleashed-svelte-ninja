import type { PageLoad } from './$types';

export const load = (async ({ fetch, setHeaders }) => {
	const res = await fetch('http://127.0.0.1:8000/api/five-acts/');
	const data = await res.json();

	const actsOfKindness = data.map((act) => act.fields);

	setHeaders({
		'Access-Control-Allow-Origin': '*'
	});

	return {
		actsOfKindness
	};
}) satisfies PageLoad;
