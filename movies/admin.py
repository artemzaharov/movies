from django.contrib import admin

# Register your models here.
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews

#this is how wr register our models from models.py in admin to see theme in www........../admin
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)