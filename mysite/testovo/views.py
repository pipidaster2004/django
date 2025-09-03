from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import BookForm
from rest_framework import generics, viewsets
from .serializers import BookSerializer, AuthorSerializer


def index(request):
    """
    начальная страница
    """
    return HttpResponse("начальная страница, перейти на /bd/, чтобы увидеть данные в бд, на /bda/ чтобы добавить книгу.")

def add_book(request):
    """
    представление добавления новой книги
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'testovo/add_book.html', {'form': form})


def book_list(request):
    """
    получение списка всех книг
    """
    books = Book.objects.all()  # Получаем все книги
    return render(request, 'testovo/book_list.html', {'books': books})

class BookAPIView(viewsets.ModelViewSet):
    """
    получение всех книг
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorAPIView(viewsets.ModelViewSet):
    """
    получение всех авторов
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer