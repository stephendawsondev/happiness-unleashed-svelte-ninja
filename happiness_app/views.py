from django.shortcuts import render
from django.http import HttpResponse
from acts_of_kindness.models import ActsOfKindness
import random

# Create your views here.


def index(request):
    """A view to return the homepage."""

    acts = ActsOfKindness.objects.all().filter(
        approved=True)[:5]
    random_acts = random.sample(list(acts), 4) if len(acts) > 4 else acts

    context = {
        'acts': acts,
        'random_acts': random_acts
    }

  return render(request, 'happiness_app/index.html', context)
