from django.urls import path

from viewer.views import *

urlpatterns = [
    path('', movies, name='movies'),
    path('<id>', movie_detail, name='movie_detail'),
    path('genre/', genres, name='genres'),
    path('genre/<genre_id>', movies_by_genre, name='movies_by_genre'),
]