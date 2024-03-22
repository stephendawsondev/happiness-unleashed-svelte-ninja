from django.shortcuts import render
from django.http import HttpResponse
from acts_of_kindness.models import ActsOfKindness

# Create your views here.


def index(request):
    """A view to return the homepage."""

    acts = ActsOfKindness.objects.filter(
        approved=True)[:5]

    context = {
        'acts': acts,
    }

    return render(request, 'happiness_app/index.html', context)
