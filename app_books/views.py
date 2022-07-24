from django.shortcuts import render
from django.http.response import HttpResponse

def books(request):
    return render(request, 'app_books/books.html')

def book(request, book_id):
    return render(request, 'app_books/book.html', context={'book_id': book_id })
