from django.urls import path
#we create this file!!!

from . import views

#from main urls the request go here and than to our views.py 
urlpatterns = [
    path("", views.MoviesView.as_view()),
    # we take pk as integer this argument pk we take in our get method in views.py in  MovieDetailView(View)
    #path("<int:pk>/", views.MovieDetailView.as_view()),
    #but if we whant to use url instead of pk we should write it like this
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),

]