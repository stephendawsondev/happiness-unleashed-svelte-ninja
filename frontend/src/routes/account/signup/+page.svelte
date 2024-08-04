<script lang="ts">
  import type { ActionData } from './$types';
  import getCookie  from '$lib/csrfCookie';
	import { onMount } from 'svelte';

  export let form: ActionData;
  let signupForm: HTMLFormElement;
  onMount(async () => {
    signupForm = document?.querySelector('.signup-form') || document.createElement('form');
  });

  const handleSubmit = async (e: Event) => {
  e.preventDefault();
  if (!signupForm) {
    return;
  }
  const formData = new FormData(signupForm);
  const username = formData.get('username') as string;
  const email = formData.get('email') as string;
  const password1 = formData.get('password1') as string;
  const password2 = formData.get('password2') as string;

  if (password1 !== password2) {
    form = { error: 'Passwords do not match' };
    return;
  }

  console.log(username, email, password1);

  const response = await fetch('http://localhost:8000/_allauth/browser/v1/auth/signup', {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken') || '',
    },
    credentials: 'include',
    body: JSON.stringify({ username, email, password: password1 })
  });

  console.log(response);

  if (response.ok) {
    window.location.href = '/';
  } else {
    const data = await response.json();
    form = data;
  }
};


</script>
<div class="container my-4">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center logo-font mb-4 text-pink mt-5">Sign Up</h2>
            <hr class="w-25 mx-auto">

            <form method="POST" class="signup-form" onsubmit={handleSubmit}>
                <div class="form-group">
                    <label for="username" class="--bs-pink1">Username</label>
                    <input type="username" name="username" id="username" class="form-control"
                        placeholder="Username" value={form?.username?? ''} required>
                    <small class="text-secondary">*Choose your username carefully, as it cannot be changed later on.</small>
                </div>
                <div class="form-group">
                  <label for="email" class="text-pink">Email</label>
                  <input type="email" name="email" id="email" class="form-control mb-3" placeholder="Email" value={form?.email ?? ''} required>
                </div>
                <div class="form-group">
                  <label for="password1" class="text-pink">Password</label>
                  <input type="password" name="password1" id="password1" class="form-control mb-3" placeholder="Password" required>
                </div>
                <div class="form-group">
                    <label for="password2" class="text-pink">Confirm password</label>
                    <input type="password" name="password2" id="password2" class="form-control mb-3"
                        placeholder="Confirm password" required>
                </div>
                {#if form?.error}
                <div class="alert alert-danger mt-3">
                  <ul class="list-unstyled m-0">
                    <li>{form.error}</li>
                  </ul>
                </div>
              {/if}
                <div class="form-actions text-center">
                    <button class="btn btn-lg btn-primary btn-block mt-4 -bs-purple" type="submit"
                        style="width: 80%">Confirm</button>
                </div>
          </form>

            <div class="mb-3">
                <p class="text-center">
                    Have an account? <a href="/account/signin">Sign in</a>.
                </p>
            </div>
        </div>
    </div>
</div>