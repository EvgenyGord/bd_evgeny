from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def beautiful_table(request):
     return render(request, 'horoscope/new_template.html')


def main_page(request):
     return HttpResponse("Главная страница")


zodiac_dict = {
     'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
     'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
     'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
     'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
     'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
     'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
     'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
     'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
     'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
     'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
     'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
     'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}
zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}
# def get_upper_convertor(request, sign_zodiac):
#      return HttpResponse(f'Получится - {sign_zodiac}')


# def get_split_converter(request, sign_zodiac):
#      return HttpResponse(f'Получится - {sign_zodiac}')
# def get_my_date_converters(request, sign_zodiac):
#      return HttpResponse(f"Вы передали дату - {sign_zodiac}")
#
# def get_yyyy_converters(request, sign_zodiac):
#      return HttpResponse(f"Вы передали число из 4х цифр - {sign_zodiac}")
# def get_my_float_converters(request, sign_zodiac):
#      return HttpResponse(f"Вы передали вещественное число - {sign_zodiac}")

def month_day(request, month, day):
     if not 1<=month<=12 or not 1<=day<=31:
          return HttpResponseNotFound("Неправильно введены данные")

     if (month == 3 and day in list(range(21, 32))) or (month == 4 and day in list(range(1, 21))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['aries']))
     elif (month == 4 and day in list(range(22, 31))) or (month == 5 and day in list(range(1, 22))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['taurus']))
     elif (month == 5 and day in list(range(21, 32))) or (month == 6 and day in list(range(1, 22))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['gemini']))
     elif (month == 6 and day in list(range(22, 31))) or (month == 7 and day in list(range(1, 23))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['cancer']))
     elif (month == 7 and day in list(range(23, 32))) or (month == 8 and day in list(range(1, 22))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['leo']))
     elif (month == 8 and day in list(range(22, 32))) or (month == 9 and day in list(range(1, 23))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['virgo']))
     elif (month == 9 and day in list(range(24, 31))) or (month == 10 and day in list(range(1, 24))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['libra']))
     elif (month == 10 and day in list(range(24, 32))) or (month == 11 and day in list(range(1, 23))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['scorpio']))
     elif (month == 11 and day in list(range(23, 31))) or (month == 12 and day in list(range(1, 23))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['sagittarius']))
     elif (month == 12 and day in list(range(23, 32))) or (month == 1 and day in list(range(1, 21))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['capricorn']))
     elif (month == 1 and day in list(range(21, 32))) or (month == 2 and day in list(range(1, 20))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['aquarius']))
     elif (month == 2 and day in list(range(20, 29))) or (month == 3 and day in list(range(1, 21))):
          return HttpResponseRedirect(reverse('horoscope-name', args=['pisces']))

def type_index(request):
     f = ''
     for m in zodiac_element:
          f += f'<li><a href="{m}/">{m.title()}</a></li>'
     response = f'''
                    <ul>
                         {f}
                    </ul>
                    '''
     return HttpResponse(response)

def type(request, type_name):
     l = ''
     for i in zodiac_element[type_name]:
          element_url = reverse('horoscope-name', args=[i])
          l += f'<li><a href="{element_url}">{i.title()}</a></li>'

     response = f'''
               <ul>
                    {l}
               </ul>
               '''
     return HttpResponse(response)



def index(request):
     zodiacs = list(zodiac_dict)
     # f'<li><a href="{redirect_path}">{sign.title()}</a></li>'
     context = {
          'zodiacs': zodiacs,
          'zodiac_dict': {},
     }
     return render(request, 'horoscope/index.html', context=context)




def get_info_about_sign_zodiac(request, sign_zodiac: str):

     description = zodiac_dict.get(sign_zodiac)
     data = {
          'description_zodiac': description,
          'sign': sign_zodiac,
          # 'sign_name': description.split()[0],
          'zodiacs': zodiac_dict,

     }
     return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
     zodiacs=list(zodiac_dict)
     if sign_zodiac>len(zodiacs) or sign_zodiac == 0:
          return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
     name_zodiac = zodiacs[sign_zodiac-1]
     redirect_url=reverse('horoscope-name', args=(name_zodiac,))
     return HttpResponseRedirect(redirect_url)




