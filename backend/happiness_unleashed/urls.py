"""
URL configuration for happiness_unleashed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('happiness_app.urls')),
    path('accounts/', include('allauth.urls')),
    path("_allauth/", include("allauth.headless.urls")),
    path('acts_of_kindness/', include('acts_of_kindness.urls')),
    path('profile/', include('profiles.urls')),
    path('posts/', include('post.urls')),
    path('api/', api.urls),
]

handler404 = 'happiness_unleashed.views.handler404'
handler500 = 'happiness_unleashed.views.custom_500'
