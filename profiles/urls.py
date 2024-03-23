from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.profile, name='profile'),
    path('delete/', views.account_delete, name='account_delete'),

]
