from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')
register_converter(converters.SplitConvertor, 'split_converter')
register_converter(converters.UpperConvertor, 'upper_convertor')

urlpatterns = [

    path('', views.index, name='horoscope-index'),

    path('type/', views.type_index),
    path('type/<str:type_name>/', views.type, name='type_names'),

    path('<int:month>/<int:day>', views.month_day, name='month_day'),


    # path('<split_converter:sign_zodiac>', views.get_split_converter),
    # path('<upper_convertor:sign_zodiac>', views.get_upper_convertor),
    # path('<my_date:sign_zodiac>', views.get_my_date_converters),
    # path('<yyyy:sign_zodiac>', views.get_yyyy_converters),

    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    # path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),



    # path('leo/', views_horoscope.leo),
    # path('aries/', views_horoscope.aries),
    # path('taurus/', views_horoscope.taurus),
    # path('gemini/', views_horoscope.gemini),
    # path('cancer/', views_horoscope.cancer),
    # path('virgo/', views_horoscope.virgo),
    # path('libra/', views_horoscope.libra),
    # path('scorpio/', views_horoscope.scorpio),
    # path('sagittarius/', views_horoscope.sagittarius),
    # path('capricorn/', views_horoscope.capricorn),
    # path('aquarius/', views_horoscope.aquarius),
    # path('pisces/', views_horoscope.pisces),


]