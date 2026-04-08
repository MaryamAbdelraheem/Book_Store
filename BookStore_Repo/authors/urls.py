from django.urls import path
from . import views

urlpatterns = [
    path('',          views.index, name='authors_index'),
    path('<int:author_id>/', views.show,  name='authors_show'),
]
