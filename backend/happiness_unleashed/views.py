from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token


def get_csrf_token(request):
    token = get_token(request)
    print(f"CSRF Token: {token}")
    response = JsonResponse({'csrfToken': token})
    response.set_cookie('csrftoken', token)
    return response


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def custom_500(request):
    return render(request, 'errors/500.html', status=500)
