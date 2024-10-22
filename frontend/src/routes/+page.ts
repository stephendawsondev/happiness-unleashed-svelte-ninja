import type { PageLoad } from './$types';

export const load = (async ({ fetch }) => {
	const res = await fetch('http://127.0.0.1:8000/api/five-acts');
	const actsOfKindness = await res.json();

	return {
		actsOfKindness
	};
}) satisfies PageLoad;
