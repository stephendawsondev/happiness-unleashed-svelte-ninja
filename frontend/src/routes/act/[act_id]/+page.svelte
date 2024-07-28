<script lang="ts">
  import type { Act } from '$lib/types';
  let {data} = $props();

  let { actOfKindness }: {actOfKindness: Act} = data
</script>

<div class="container my-4">
  <h2 class="text-center logo-font mb-4 text-pink mt-5">{actOfKindness.name}</h2>
  <p class="text-center">{actOfKindness.description}</p>

  {#if actOfKindness.image}
      <img src={actOfKindness.image} class="img-actOfKindness-detail img-fluid mx-auto d-block" alt={actOfKindness.name}>
  {/if}


</div>