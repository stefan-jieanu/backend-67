from django.shortcuts import render

from books.models import Book, Author


# Create your views here.
def books(request):
    books = Book.objects.all()

    return render(
        request,
        'books.html',
        context={
            'books': books
        }
    )

def book_detail(request, id):
    book = Book.objects.get(id=id)

    return render(
        request,
        'book_detail.html',
        context={
            'book': book
        }
    )

# View asociat paginii in care sunt toti autorii
def authors(request):
    a = Author.objects.all()

    return render(
        request,
        'authors.html',
        context={
            'authors': a
        }
    )

# View asociat paginii cu cartile unui autor
def books_by_author(request, author_id):
    a = Author.objects.get(id=author_id)
    b = Book.objects.filter(author=a)

    return render(
        request,
        'books_by_author.html',
        context={
            'author': a,
            'books': b
        }
    )