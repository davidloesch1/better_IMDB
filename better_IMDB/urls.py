from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('directors/', views.DirectorList.as_view(), name='director_list'),
    path('directors/<int:pk>', views.DirectorDetail.as_view(),
         name='director_detail'),
    path('actors/', views.ActorList.as_view(), name='actor_list'),
    path('actors/<int:pk>', views.ActorDetail.as_view(), name='actor_detail'),
    path('genres/', views.GenreList.as_view(), name='genre_list'),
    path('genres/<int:pk>', views.GenreDetail.as_view(), name='genre_detail')
]
