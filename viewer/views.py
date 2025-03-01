from django.http import HttpResponse
from django.shortcuts import render

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

def movies(request):
    # Query database to get all movies
    movies = Movie.objects.all()

    # Filter by field value
    # movies = Movie.objects.filter(rating=8)

    # genre = Genre.objects.get(name='Horror')
    # movies = Movie.objects.filter(genre=genre)

    # movies = Movie.objects.filter(genre__name='Horror')

    # movies = Movie.objects.filter(rating=8).filter(genre__name='Comedy')
    # sau
    # movies = Movie.objects.filter(rating=8)
    # movies = movies.filter(genre__name='Comedy')

    movies = movies.order_by('-rating')

    return render(
        request,
        'movies.html',
        context={'movies': movies}
    )

def movie_detail(request, id):
    movie = Movie.objects.get(id=id)

    return render(
        request,
        'movie_detail.html',
        context={
            'movie': movie
        }
    )

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

def genres(request):
    g = Genre.objects.all()

    return render(
        request,
        'genres.html',
        context={
            'genres': g
        }
    )
