from django.urls import path
from . import views as views_week_days
urlpatterns = [
    path('<int:days_week>', views_week_days.get_info_about_week_days_number),
    path('<str:days_week>', views_week_days.get_info_about_week_days, name='week_days-name'),
    # path('tuesday/', views_week_days.tuesday),
    # path('monday/', views_week_days.monday),

]