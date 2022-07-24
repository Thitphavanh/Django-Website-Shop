from django.shortcuts import render
from django.http.response import HttpResponse


all_books = [
    {'id': 1, 'title': 'Steve Jobs by Walter Isaacson', 'price': 320000, 'is_hardcover': True},
    {'id': 2, 'title': 'Elon Musk', 'price': 120000, 'is_hardcover': False},
    {'id': 3, 'title': 'Leonardo da Vinci by Walter Isaacson', 'price': 320000, 'is_hardcover': True},
    {'id': 4, 'title': 'Einstein, His Life and Universe', 'price': 320000, 'is_hardcover': False},

]


def books(request):
    context = { 'books': all_books}
    return render(request, 'app_books/books.html',context)


def book(request, book_id):
    return render(request, 'app_books/book.html', context={'book_id': book_id})
