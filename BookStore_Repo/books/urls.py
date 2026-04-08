from django.urls import path
from . import views

urlpatterns = [
    path('',          views.index, name='books_index'),
    path('<int:book_id>/', views.show,  name='books_show'),
]
