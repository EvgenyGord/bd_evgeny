import random

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import random
# Create your views here.
def page_main(request):
    posts = [
        {
            'title': 'Рыбалка',
            'description': 'Хорошо посидели',
            'date': '21 авг 2021',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
        },
        {
            'title': 'Париж',
            'description': 'Незабываемое путешествие',
            'date': '5 сент 2020',
            'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                    Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
        },
        {
            'title': 'Финал лиги чемпионов',
            'description': 'Реал опять выиграл ЛЧ',
            'date': '28 мая 2022',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
        },
        {
            'title': 'Охота на уток',
            'description': 'Ни одна утка не пострадала',
            'date': '7 дек 2019',
            'content': 'Lorem ipsum dolor sit amet.'
        },
        {
            'title': 'Фестиваль огурца',
            'description': 'Суздаль ждет тебя',
            'date': '12 июль 2021',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
        },
        {
            'title': 'Нашествие',
            'description': 'Даешь рок, но в следующем году',
            'date': '29 июль 2021',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
        },
        {
            'title': 'Новый год',
            'description': 'Эх, еще один год пролетел',
            'date': '31 дек 2022',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
        },
    ]
    random.shuffle(posts)
    context={
        'posts': posts[:3],
    }
    return render(request, 'blog/index.html', context=context)
def posts(request):
    return render(request, 'blog/list_detail.html')
def praktika(request):
    data = {
        'year_born': '1964 г.',
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'blog/praktika.html', context=data)
def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)
def get_info_about_posts(request, name_post):
    data = {
        'name': name_post
    }
    return render(request, 'blog/detail_by_name.html', context=data)
def get_info_about_posts_number(request, number_post):
    data = {
        'number':number_post
    }
    return render(request, 'blog/detail_by_number.html', context=data)