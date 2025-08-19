from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def index(request):
    return HttpResponse("начальная страница, перейти на /bd/, чтобы увидеть данные в бд, на /bda/ чтобы добавить книгу.")

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'testovo/add_book.html', {'form': form})


def book_list(request):
    books = Book.objects.all()  # Получаем все книги
    return render(request, 'testovo/book_list.html', {'books': books})