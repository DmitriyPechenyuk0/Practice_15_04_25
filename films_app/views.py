from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse,HttpResponse
from .models import Film
from .forms import ReviewForm

# Create your views here.

def render_all_films(request: HttpRequest):
    all_films = Film.objects.all()
    films = Film.objects.filter(genre = 'Бойовик')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            return JsonResponse({'success': True, 'message' : "Форма успішно відправлена"})
        else:
            pass
    else:
        form = ReviewForm()
    # 
    return render(
        request= request, 
        template_name = 'films_app/film.html',
        context= {
            "films": all_films,
            "form": form,
            'filtered': films
        }
    )

def add_to_favourite(request: HttpRequest, film_pk: int):
    response = redirect("all_films")
    all_cookies = request.COOKIES.get("favourites")
    if all_cookies:
        if film_pk not in all_cookies:
            all_cookies += ' ' + str(film_pk)
            # film = Film.objects.get(film_pk)
            # film.favourite = True
            # film.save()
    else:
        all_cookies = str(film_pk)
    response.set_cookie("favourites", all_cookies)
    return response 


def render_favourite_films(request):
    all_cookies = request.COOKIES.get("favourites")
    if all_cookies:
        list_favourites_pk =  all_cookies.split(" ")
        objects_favourite_films = Film.objects.filter(pk__in = list_favourites_pk)
    else:
        objects_favourite_films = []
    return render(request, 'films_app/favourite_film.html', {"objects_favourite_films": objects_favourite_films} )

def get_by_filter(request): 
    genre_list = request.GET.get('genres')

    if genre_list:
        genres = genre_list.split('-')
        films = Film.objects.filter(genre__in=genres)
    else:
        genres = []
        films = Film.objects.all()
    
    film_data = []

    for film in films:
        film_data.append({
            'name': film.name,
            'image': film.image.url,
            'genre': film.genre,
            'description': film.description
        })
    
    return JsonResponse({'films': film_data})