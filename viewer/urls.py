from django.urls import path

from viewer.views import *

urlpatterns = [
    # Daca folosim Class Based Views, trebuie sa apelam func .as_view()
    path('', MoviesView.as_view(), name='movies'),

    # Pentru un detail view avem nevoie de o variabila <pk> in url
    # DetailView sa va folosit automat de acea variabila pentru a gasi
    # un obiect in baza de date
    path('<pk>', MoviesDetailView.as_view(), name='movie_detail'),
    path('genre/', GenresView.as_view(), name='genres'),
    path('genre/<genre_id>', movies_by_genre, name='movies_by_genre'),
    path('create/', MovieCreateView.as_view(), name='movie_create')
]