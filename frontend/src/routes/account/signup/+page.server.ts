// +page.server.ts
import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';
import { signUp } from '$lib/allauth';

export const actions: Actions = {
	signup: async ({ request, fetch }) => {
		const data = await request.formData();
		const username = data.get('username') as string;
		const email = data.get('email') as string;
		const password1 = data.get('password1') as string;
		const password2 = data.get('password2') as string;
		const csrfmiddlewaretoken = data.get('csrf_token') as string;

		if (password1 !== password2) {
			return fail(400, { error: 'Passwords do not match' });
		}
		try {
			const response = await signUp(
				{ username, email, password: password1, csrfmiddlewaretoken },
				{ fetch }
			);
			console.log('Full response:', response);

			if (response.status === 200) {
				return redirect(303, '/account');
			} else if (response.status === 400) {
				return fail(400, { error: response.errors[0].message });
			} else {
				return fail(500, { error: 'An error occurred' });
			}
		} catch (error) {
			console.error('Signup error:', error);
			return fail(500, { error: 'An error occurred' });
		}
	}
};
