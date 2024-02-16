from django.urls import path
from . import views
urlpatterns = [
    path('', views.my_information, name='information'),
    path('education', views.my_education, name='education'),
    path('programming', views.my_programming, name='programming'),
]