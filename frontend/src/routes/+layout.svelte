<script lang="ts">
	import type { Snippet } from 'svelte';
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte';

  let { children }: { children: Snippet } = $props();
</script>
  <Header />

  <main class="flex-shrink-0">
    {@render children()}
  </main>

<Footer />
  
