import { browser } from '$app/environment';
import { getCsrfToken } from './csrfCookie';

const Client = Object.freeze({
	APP: 'app',
	BROWSER: 'browser'
});

const CLIENT = Client.BROWSER;

const BASE_URL = `http://localhost:8000/_allauth/${CLIENT}/v1`;
const ACCEPT_JSON = {
	accept: 'application/json'
};

export const AuthProcess = Object.freeze({
	LOGIN: 'login',
	CONNECT: 'connect'
});

export const Flows = Object.freeze({
	LOGIN: 'login',
	SIGNUP: 'signup'
});

export const URLs = Object.freeze({
	// Meta
	CONFIG: BASE_URL + '/config',

	// Account management
	EMAIL: BASE_URL + '/account/email',

	// Auth: Basics
	LOGIN: BASE_URL + '/auth/login',
	SESSION: BASE_URL + '/auth/session',
	REAUTHENTICATE: BASE_URL + '/auth/reauthenticate',
	SIGNUP: BASE_URL + '/auth/signup',

	// Auth: Sessions
	SESSIONS: BASE_URL + '/auth/sessions'
});

async function request(method, path, data = {}, headers = {}, event = null) {
	const options = {
		method,
		headers: {
			...ACCEPT_JSON,
			...headers
		},
		credentials: 'include'
	};

	if (typeof data !== 'undefined') {
		options.body = JSON.stringify(data);
		options.headers['Content-Type'] = 'application/json';
	}

	const fetchFn = event ? event.fetch : fetch;
	const resp = await fetchFn(path, options);
	const msg = await resp.json();
	return msg;
}

export async function login(data, event = null) {
	return await request('POST', URLs.LOGIN, data, {}, event);
}

export async function reauthenticate(data, event = null) {
	return await request('POST', URLs.REAUTHENTICATE, data, {}, event);
}

export async function logout(event = null) {
	return await request('DELETE', URLs.SESSION, {}, {}, event);
}

export async function signUp(data, event = null) {
	const csrfToken = await getCsrfToken();
	const headers = csrfToken ? { 'X-CSRFToken': csrfToken } : {};
	return await request('POST', URLs.SIGNUP, data, headers, event);
}

export async function getEmailAddresses(event = null) {
	return await request('GET', URLs.EMAIL, {}, {}, event);
}

export async function getSessions(event = null) {
	return await request('GET', URLs.SESSIONS, {}, {}, event);
}

export async function endSessions(ids, event = null) {
	return await request('DELETE', URLs.SESSIONS, { sessions: ids }, {}, event);
}

export async function getConfig(event = null) {
	return await request('GET', URLs.CONFIG, {}, {}, event);
}

export async function addEmail(email, event = null) {
	return await request('POST', URLs.EMAIL, { email }, {}, event);
}

export async function deleteEmail(email, event = null) {
	return await request('DELETE', URLs.EMAIL, { email }, {}, event);
}

export async function markEmailAsPrimary(email, event = null) {
	return await request('PATCH', URLs.EMAIL, { email, primary: true }, {}, event);
}
