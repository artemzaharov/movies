from django.shortcuts import render
#we import this for use Class Based Views
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

# Create your views here.

from .models import Movie

#Class Based Views https://djbook.ru/rel1.9/ref/class-based-views/base.html
class MoviesView(ListView):
    #and this will work with class MoviesView(View): but we rewrite them
    '''def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list':movies}) '''
    # we use ListView
    model = Movie
    #here we take draft from models not to show films wich are not ready to show on site and change queryset = Movie.objects.all() to
    queryset = Movie.objects.filter(draft=False)
    #template_name = 'movies/movies.html'
        

class MovieDetailView(DetailView):
    '''full film discription
    pk is a num that we give in our url(primary key)
    def get(self, request, pk):
        we gave request to our sql base , get method take one record(запись) and compare id and pk
        movie = Movie.objects.get(id=pk)
        return render(request,'movies/movie_detail.html',{'movie':movie})'''
    #so it is not good idea to use pk because it is not human readible lets use url
    #and this will work with class MoviesView(View): but we rewrite them to DetailView
    '''
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request,'movies/movie_detail.html',{'movie':movie})'''
    
    model = Movie
    #what field to look for 
    slug_field = 'url'
