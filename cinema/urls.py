from django.urls import path

from .views import MovieListView, ActorListView, ActorCreateView, MovieCreateView

urlpatterns = [
    path('actors/', ActorListView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('create-actor/', ActorCreateView.as_view()),
    path('create-movie/', MovieCreateView.as_view())
]