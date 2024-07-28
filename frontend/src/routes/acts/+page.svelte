<script lang="ts">
import type { Act } from '$lib/types';

let { data } = $props();


let { actsOfKindness }: {actsOfKindness:  Act[]} = data


console.log(actsOfKindness)
</script>

<section class="py-5" id="acts-list-section">
  <div class="container">
      <div class="d-flex justify-content-start align-items-center">
          <h1>Acts of Kindness</h1>
          <!-- <a href="{ 'add_act' }" class="btn btn-primary d-block ms-2">Add Act of Kindness</a> -->
      </div>
      {#if actsOfKindness }
      <div class="d-flex flex-wrap mt-4 gap-3 justify-content-around cards-container">
      {#each actsOfKindness as act}
        <div class="card">
            <div class="card-header p-0">
                {#if act.image }
                <img src="{ act.image }" alt="{ act.name } image" class="card-img-top">
                {/if}
            </div>
            <div class="card-body">
                <p>{ act.description }</p>
            </div>
            <div class="d-grid gap-2 px-3 pb-3">
                <a href="acts/{act.id}"  class="btn btn-primary" type="button">View</a>
            </div>
        </div>
      {/each}
      </div>
      {:else}
      <p>No acts of kindness found.</p>
      {/if}
  </div>

</section>