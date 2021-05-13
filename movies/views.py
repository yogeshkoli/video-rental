from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def details(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'movies/details.html', {'movie': movie})
    except Movie.DoesNotExist:
        raise Http404()
