from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from viewer.forms import MovieForm
from viewer.models import Movie, Genre


# Create your views here.
def hello(request):
    title = 'Hollywood'
    user = 'Vasile'
    movies = ['Star Wars', 'Saw']

    return render(
        request,
        'hello.html',
        context={
            'title': title,
            'user': user,
            'movies': movies
        }
    )

def home(request):
    return render(
        request,
        'home.html',
        context={}
    )

# Exemplu de view cu parametru tip regular expression
def param_reg(request, s):
    return HttpResponse(f'Hello {s}!')

# Exemplu de view cu parametru url encoded
def param_url(request):
    # request va contine toate datele request-ului
    # request.GET va contine un QueryDict cu datele din url
    # pentru link-ul: http://127.0.0.1:8000/param-url/?nume=Ana&varsta=24
    # request.GET va fi: <QueryDict: {'nume': ['Ana'], 'varsta': ['24']}>
    name = request.GET.get('nume', '')
    age = request.GET.get('varsta', '')
    return HttpResponse(f'Eu sunt {name} si am {age} ani.')

# def movies(request):
#     # Query database to get all movies
#     movies = Movie.objects.all()
#
#     # Filter by field value
#     # movies = Movie.objects.filter(rating=8)
#
#     # genre = Genre.objects.get(name='Horror')
#     # movies = Movie.objects.filter(genre=genre)
#
#     # movies = Movie.objects.filter(genre__name='Horror')
#
#     # movies = Movie.objects.filter(rating=8).filter(genre__name='Comedy')
#     # sau
#     # movies = Movie.objects.filter(rating=8)
#     # movies = movies.filter(genre__name='Comedy')
#
#     movies = movies.order_by('-rating')
#
#     return render(
#         request,
#         'movies.html',
#         context={'movies': movies}
#     )

# O clasa de View generica in care trebuie implementat de noi tot codul
# class MoviesView(View):
#     def get(self, request):
#         m = Movie.objects.all()
#         return render(
#             request,
#             'movies.html',
#             context={'movies': m}
#         )

# Un TemplateView generic in care specificam un template si un context
# class MoviesView(TemplateView):
#     # Template-ul de HTML folosit
#     template_name = 'movies.html'
#
#     # Contextul pus in interiorul template-ului
#     extra_context = {'movies': Movie.objects.all()}

# Un ListView este folosit specific pentru a afisa toate obiectele
# intr-un template de HTML
class MoviesView(ListView):
    template_name = 'movies.html'

    # Modelul afisat in acest view
    model = Movie

# def movie_detail(request, id):
#     movie = Movie.objects.get(id=id)
#
#     return render(
#         request,
#         'movie_detail.html',
#         context={
#             'movie': movie
#         }
#     )

# Un detail view este folosit pentru a afisa un singur obiect
# LoginRequiredMixin obliga utilizatorul sa fie autentificat
# PermissionRequiredMixin verifica permisiunea specificata in view
class MoviesDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'movie_detail.html'

    # Modelul afisat in pagina
    model = Movie

    # Permisiunile se scriu sub forma
    # numeaplicatie.numeactiune_numemodel
    # actiunile pot fi: view, add, change, delete
    permission_required = 'viewer.view_movie'

def movies_by_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    movies = Movie.objects.filter(genre=genre)

    return render(
        request,
        'movies_by_genre.html',
        context={
            'genre': genre,
            'movies': movies
        }
    )

# def genres(request):
#     g = Genre.objects.all()
#
#     return render(
#         request,
#         'genres.html',
#         context={
#             'genres': g
#         }
#     )
class GenresView(ListView):
    template_name = 'genres.html'
    model = Genre

# View pentru un form generic
# Putem face orice cu datele din acest view
# (sa le salvam in DB, sa trimitem un mail cu ele, etc)
# class MovieCreateView(FormView):
#     template_name = 'movie_form.html'
#     form_class = MovieForm
#
#     # Pagina pe care suntem trimisi dupa ce completam formularul
#     success_url = reverse_lazy('movies')
#
#     # Functia se va apela automat in cazul in care formularul primit
#     # este valid
#     def form_valid(self, form):
#         result = super().form_valid(form)
#
#         # form.cleaned_data este un dictionar cu datele din formular
#         cleaned_data = form.cleaned_data
#
#         Movie.objects.create(
#             title=cleaned_data['title'],
#             genre=cleaned_data['genre'],
#             rating=cleaned_data['rating'],
#             released=cleaned_data['released'],
#             description=cleaned_data['description']
#         )
#
#         return result
#
#     # Daca formularul nu este valid, se va apelac func:
#     def form_invalid(self, form):
#         print('Formularul nu este valid!')
#         return super().form_invalid(form)

class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.change_movie'


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'
