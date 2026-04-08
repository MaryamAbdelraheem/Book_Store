from django.urls import path
from . import views

urlpatterns = [
    path('',         views.index,   name='contactus_index'),
    path('success/', views.success, name='contactus_success'),
]
