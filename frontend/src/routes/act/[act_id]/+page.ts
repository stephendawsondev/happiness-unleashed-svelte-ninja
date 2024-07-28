export const load = async ({ params }) => {
	const { act_id } = params;
	const res = await fetch(`http://127.0.0.1:8000/api/act/${act_id}`);
	const actOfKindness = await res.json();
	return {
		actOfKindness
	};
};
