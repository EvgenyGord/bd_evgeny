from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.All_directors.as_view()),
    path('directors/<int:pk>', views.One_director.as_view(), name='director-detail'),
    path('actors', views.All_actors.as_view()),
    path('actors/<int:pk>', views.One_actor.as_view(), name='actor-detail'),
]