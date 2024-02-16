from . import views
from django.urls import path

urlpatterns = [
    path('load_image', views.CreateGalleryView.as_view()),
    path('list_image', views.ListGallery.as_view()),
]