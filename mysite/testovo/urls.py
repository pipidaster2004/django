from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bd/", views.book_list, name="book_list"),
    path("bda/", views.add_book, name="add_book"),
]