# coding: utf-8
from movie_app.models import Movie
Movie.objects.all()
Movie.objects.all()[2]
dj=Movie.objects.all()[2]
dj.year=2014
dj.budjet=99999999999
