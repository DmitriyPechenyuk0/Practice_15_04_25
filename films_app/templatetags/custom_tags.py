from django import template
from films_app.models import Film


# Створюємо об'єкт для реестрації тегів
register = template.Library()

# Реєструємо прстий тег, що повертає значення
@register.simple_tag
# Створюємо функцію тегу, що рахує та повретає улюблені фильмі
def count_favourite_films(request):
    # Отримуємо кукі з pk улюблених фільмів
    all_cookies = request.COOKIES.get("favourites")
    # Ставимо дефолтне значення улюблених фільмів
    count_favourite_films = 0
    # Створюємо умову якщо є кукі
    if all_cookies:
        # Створюємо список та сплітуємо по пробілу, ти самим утворюючи список з pk улюблених фільмів
        list_favourites_pk = all_cookies.split(" ")
        # Створюємо об'єкт лічильника кукі
        count_favourite_films = len(list_favourites_pk)
    # Повертаємо лічильник улюблених фільмів 
    return count_favourite_films
 
# Реєструємо кастомний тег, що включає у собі HTML-шаблон 
@register.inclusion_tag('films_app/inclusion_tags/best_film.html')
# створюємо функцію тегу
def best_film():
    #створюємо та отримуємо об'єкт з ключем 
   film = Film.objects.get(pk = 2) 
    #Передаємо об'єкт фільму у best_film.html
   return {'film': film}

# Реєструємо кастомний тег, що включає у собі HTML-шаблон 
@register.inclusion_tag('films_app/inclusion_tags/films_render.html')
# створюємо функцію тегу
def films_render(films):
    # повертаємо значення списку фільмів films_render.html
    return {'films': films}
    

@register.inclusion_tag('films_app/inclusion_tags/filters.html')
def filters():
    films = Film.objects.all()
    genres = []
    for film in films:
        if film.genre not in genres:
            genres.append(film.genre)
    return {'genres': genres}