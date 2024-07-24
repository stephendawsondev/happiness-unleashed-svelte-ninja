
<section class="py-4" id="acts-of-kindness-slider">
  <div class="jumbotron jumbotron-fluid">
    <div class="container hero-container py-2 bg-primary text-white rounded">
      <div class="mx-2">
        <h1 class="display-4 hero-text text-light">Make Today Kindness-Filled!</h1>
        <p class="lead text-white">Every Gesture Counts: Let's Fill Today with Acts of Kindness</p>
      </div>
      <img src="https://res.cloudinary.com/dyoueyepq/image/upload/v1711370131/ppojioat3zpqm8hg3apu.png" class="hero-img" alt="Image of hand holding a kind note">
    </div>
  </div>
</section>
<section class="pb-5" id="acts-of-kindness-cards">
  <div class="container py-3 overflow-hidden">
    <h3 class="text-left">Choose a Random Act of Kindness!</h3>
    <div class="swiper-container mt-2">
      <div class="swiper-wrapper">
        <!-- {% for act in random_acts %} -->
        <div class="swiper-slide">
          <div class="card mb-3" style="max-width: 300px; height: 520px;">
            <!-- {% if act.image %} -->
            <!-- <img src="{{ act.image.url }}" class="card-img-top" alt="{{ act.name }}"> -->
            <!-- {% else %} -->
            <!-- <img src="{% static 'path/to/default/image.jpg' %}" class="card-img-top" alt="Default Image"> -->
            <!-- {% endif %} -->
            <div class="card-body">
              <!-- <h5 class="card-title">{{ act.name }}</h5> -->
              <!-- <p class="card-text">{{ act.description|truncatewords:12 }}</p> -->
            </div>
            <div class="d-grid gap-2 px-3 pb-3">
              <!-- <a href={% url 'act_detail' act.id %} <button class="btn btn-primary" type="button">View</button></a> -->
            </div>
          </div>
        </div>
        <!-- {% endfor %} -->
      </div>
    </div>
  </div>
</section>


