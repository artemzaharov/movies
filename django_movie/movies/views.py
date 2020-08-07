from django.shortcuts import render, redirect
#we import this for use Class Based Views
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm
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

class AddReview(View):

    def post(self, request, pk):
        #django write our form with date from browser and Post reuest
        form = ReviewForm(request.POST)
        #we take object of movie with django ORM
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            # commit False means that we should stop our form saving for some time
            form = form.save(commit=False)
            #lets add parent to our comment answer, 'parent' is name of   <input type='hidden' name='parent' id='contactparent' value=''> 
            if request.POST.get('parent', None):
                #if we find parent name so we make this code if not we dont find it will be None
                #the 'parent' is a string so we should make it int,
                form.parent_id = int(request.POST.get('parent'))

            # we take movie_id from table movies_rewiews it is a table wich we create after migrations of models.py class Reviews(models.Model): 
            # movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)
            '''form.movie_id = pk'''
            #this variant works with movie = Movie.objects.get(id=pk) and the hayer varint works without it
            form.movie = movie
            form.save()
            #Here we get self url to redirect us to our film after we input review to film
            return redirect(movie.get_absolute_url())

        
