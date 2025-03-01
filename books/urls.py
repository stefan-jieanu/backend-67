from django.urls import path

from books.views import books, book_detail, authors, books_by_author

urlpatterns = [
    path('', books, name='books'),
    path('<id>', book_detail, name='book_detail'),

    # Path catre pagina cu toti autorii
    path('authors/', authors, name='authors'),

    # Path catre pagina cu toate cartile unui autor
    path('authors/<author_id>', books_by_author, name='books_author')
]