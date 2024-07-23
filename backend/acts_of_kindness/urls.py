from django.urls import path
from . import views

urlpatterns = [
    path('acts/', views.acts_list, name='acts_list'),
    path('act/<int:pk>/', views.act_detail, name='act_detail'),
    path('add/', views.add_act, name='add_act'),
    path('edit/<int:pk>/', views.edit_act, name='edit_act'),
    path('delete/<int:pk>/', views.delete_act, name='delete_act'),
    path('complete_and_share_act/<int:act_id>/', views.complete_and_share_act, name='complete_and_share_act')
]