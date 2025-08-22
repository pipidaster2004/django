from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bd/", views.book_list, name="book_list"),
    path("bda/", views.add_book, name="add_book"),
    path("genb/", views.BookAPIView.as_view(), name="book_generic"),
    path("gena/", views.AuthorAPIView.as_view(), name="author_generic"),
]