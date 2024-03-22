from django.shortcuts import render
from django.http import HttpResponse
from acts_of_kindness.models import ActsOfKindness
import random

# Create your views here.


def index(request):
    acts = ActsOfKindness.objects.all()
    random_acts = random.sample(list(acts), 4) if len(acts) > 4 else acts
    return render(request, 'happiness_app/index.html', {'random_acts': random_acts})
