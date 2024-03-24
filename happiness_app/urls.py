from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('our-team/', views.our_team, name='our_team'),
]
