from . import views
from django.urls import path

urlpatterns = [
    path('list', views.ListFeedBack.as_view()),
    path('done', views.DoneView.as_view()),
    path('', views.FeedBackView.as_view()),
    path('<int:id_feedback>', views.FeedBackUpdateView.as_view()),
    path('detail/<int:pk>', views.DetailFeedBack.as_view(), name='feed'),
    path('update/<int:pk>', views.FeedBackViewUpdate.as_view()),
]