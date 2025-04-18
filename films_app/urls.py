from .views import *
from django.urls import path

urlpatterns = [
    path('all/', render_all_films, name = 'all_films'),
    path('add-to-favourites/<film_pk>', add_to_favourite, name = 'add_to_favourite'),
    path('favourites/', render_favourite_films, name= 'favourites'),
    path('get-by-filter/', get_by_filter, name='get_by_filter')
]