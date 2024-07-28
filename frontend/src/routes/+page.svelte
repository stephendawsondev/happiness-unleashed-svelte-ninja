<script lang="ts">
  import type { Act } from '$lib/types';

  let { data } = $props();


  let { actsOfKindness }: {actsOfKindness:  Act[]} = data
</script>
<section class="py-4" id="acts-of-kindness-slider">
  <div class="jumbotron jumbotron-fluid">
    <div class="container hero-container py-2 bg-primary text-white rounded">
      <div class="mx-2">
        <h1 class="display-4 hero-text text-light">Make Today Kindness-Filled!</h1>
        <p class="lead text-white">Every Gesture Counts: Let's Fill Today with Acts of Kindness</p>
      </div>
      <img src="https://res.cloudinary.com/dyoueyepq/image/upload/v1711370131/ppojioat3zpqm8hg3apu.png" class="hero-img" alt="hand holding a kind note">
    </div>
  </div>
</section>
{#if actsOfKindness.length > 0}
<section class="pb-5" id="acts-of-kindness-cards">
  <div class="container py-3 overflow-hidden">
    <h3 class="text-left">Choose a Random Act of Kindness!</h3>
    <div class="swiper-container mt-2">
      <div class="swiper-wrapper d-flex gap-3">
        {#each actsOfKindness as act}
        <div class="swiper-slide">
          <div class="card mb-3 " style="max-width: 300px; height: 520px;">
            {#if act.image}
            <img src="{ act.image }" class="card-img-top" alt="{ act.name }">
            {:else}
            <!-- <img src="#" class="card-img-top" alt="Default Image"> -->
            {/if}
            <div class="card-body">
              <h5 class="card-title">{ act.name }</h5>
              <p class="card-text">{ act.description.split(' ').splice(0, 16).join(" ") }...</p>
            </div>
            <div class="d-grid gap-2 px-3 pb-3">
                <a href="act/{act.id}"  class="btn btn-primary" type="button">View</a>
            </div>
          </div>
        </div>
        {/each}
      </div>
    </div>
  </div>
</section>
{/if}


