from django.shortcuts import render
from django.http import HttpResponse


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def custom_500(request):
    return render(request, 'errors/500.html', status=500)


