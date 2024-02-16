from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('<str:name>', views.get_template),
    path('rectangle/<int:ширина>/<int:высота>', views.rectangle, name='rectangle'),
    path('square/<int:ширина>', views.square, name='square'),
    path('circle/<int:радиус>', views.circle, name='circle'),
    path('get_rectangle_area/<int:ширина>/<int:высота>', views.get_rectangle_area),
    path('get_square_area/<int:ширина>',  views.get_square_area),
    path('get_circle_area/<int:радиус>', views.get_circle_area),


]