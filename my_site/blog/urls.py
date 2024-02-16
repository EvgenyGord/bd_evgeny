from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('praktika', views.praktika),
    path('praktika2', views.get_guinness_world_records),
    path('', views.posts),
    path('<int:number_post>', views.get_info_about_posts_number),
    path('<name_post>/', views.get_info_about_posts),
]
