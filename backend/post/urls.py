from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:aok_pk>/add/', views.add_post, name='add_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/',
         views.delete_post, name='delete_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
