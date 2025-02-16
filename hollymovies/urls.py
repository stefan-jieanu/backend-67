"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import hello, home, param_reg, param_url, movies, movie_detail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello, name='hello'),
    path('', home, name='home'),

    # Exemplu de parametru folosind regular expressions
    path('param-regular/<s>', param_reg),

    # Exemplu cu parametru url encoded
    path('param-url/', param_url),

    path('movies/', movies, name='movies'),
    path('movies/<id>', movie_detail, name='movie_detail')
]
