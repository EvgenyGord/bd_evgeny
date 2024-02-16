from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def get_rectangle_area(request, высота: int, ширина: int):
    redirect_url_rectangle=reverse('rectangle', args=[высота,ширина])
    return HttpResponseRedirect(redirect_url_rectangle)


def get_square_area(request, ширина: int):
    redirect_url_square = reverse('square', args=[ширина])
    return HttpResponseRedirect(redirect_url_square)


def get_circle_area(request, радиус: int):
    redirect_url_circle = reverse('circle', args=[радиус])
    return HttpResponseRedirect(redirect_url_circle)


def rectangle(request, высота: int, ширина: int):
    return HttpResponse(f"Площадь прямоугольника размером {высота}x{ширина} равна {высота * ширина}")


def square(request, ширина: int):
    return HttpResponse(f"Площадь квадрата размером {ширина}x{ширина} равна {ширина * ширина}")


def circle(request, радиус: int):
    return HttpResponse(f"Площадь круга радиуса {радиус} равна {3.14 * радиус * радиус}")

def get_template(request, name: str):
    if name == 'rectangle':
        return render(request, 'geometry/rectangle.html')
    elif name== 'square':
        return render(request, 'geometry/square.html')
    elif name== 'circle':
        return render(request, 'geometry/circle.html')
    else:
        return HttpResponse('Неизвестный шаблон')
