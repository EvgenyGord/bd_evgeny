from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value

# Create your views here.
from .models import Movie, Director, Actor
from django.views.generic import ListView, DetailView

def show_all_movie(request):
    #movies = Movie.objects.order_by(F('year').desc(nulls_first=True))
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget')+100,
        ffff=F('rating')*F('year'),

    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
    })

def show_one_movie(request, slug_movie:str):
    #movie = Movie.objects.get(id=id_movie)
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie':movie
    })

# def show_directors(request):
#     directors = Director.objects.all
#     context = {
#         'directors': directors
#     }
#     return render(request, 'movie_app/all_directors.html', context=context)

# def show_one_director(request, id_dir:int):
#     director = get_object_or_404(Director, id=id_dir)
#     return render(request, 'movie_app/one_director.html', {
#         'director': director
#     })

# def show_actors(request):
#     actors = Actor.objects.all
#     context={
#         'actors': actors
#     }
#     return render(request, 'movie_app/all_actors.html', context=context)

# def show_one_actor(request, id_act: int):
#     actor = get_object_or_404(Actor, id=id_act)
#     return render(request, 'movie_app/one_actor.html', {
#         'actor': actor
#     })

class All_actors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'

class All_directors(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'

class One_actor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor

class One_director(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director
