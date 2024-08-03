<script lang="ts">
  import type { ActionData } from './$types';

  export let form: ActionData;
</script>
<div class="container my-4">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center logo-font mb-4 text-pink mt-5">Sign Up</h2>
            <hr class="w-25 mx-auto">

            <form action="?/signup" method="POST" class="signup-form">
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