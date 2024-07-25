<script lang="ts">

let { data } = $props();
let { posts } = data
</script>

<section class="py-4" id="post-list-section">
  <div class="container mb-1">
    <div class="px-1 border-bottom border-primary border-1">
      <h1>User-submitted posts</h1>
      <p class="text-secondary">Would you like to share how you have shared happiness recently? Login, select a kindness and post it to inspire others!</p>
    </div>

    {#if posts.length > 0}
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mt-3">
      {#each posts as post}
      <div class="col">
        <div class="card">
          {#if post.image_url}
          <img src={post.image_url} class="card-img-top" alt={post.title}>
          {/if}
          <div class="card-body">
            <h5 class="card-title">{post.title}</h5>
            <p class="card-text">{post.content}</p>
            <!-- <p class="card-text"><small class="text-muted">By <span class="card-author">{post.user_profile.user.username}</span> on {post.created_at}</small></p> -->
          </div>
          <div class="card-footer d-flex justify-content-between align-items-center">
            <a href={`/posts/${post.id}`} class="btn btn-primary">Read more</a>
            <p class="m-0"><span class="btn-primary custom-act-of-kindness"><i class="fas fa-star" style="color: green;"></i> {post.act_of_kindness} </span></p>
          </div>
        </div>
      </div>
      {/each}
    </div>
    {/if}
  </div>
</section>