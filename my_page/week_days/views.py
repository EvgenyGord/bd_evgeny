from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# def monday(request):
#     return HttpResponse('<h1 style="color:blue; text-align:center;">План на понедельник:</h1><br><img style="position: relative; bottom: 10px; left: 585px; height: 200px; width:300px" src="https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666287049_10-mykaleidoscope-ru-p-otkritka-s-ponedelnikom-smeshnaya-vkontakt-10.jpg"><br><p style="color:red; font-size:30px; text-align:center;" ;>1.Умыться и не лениться</p>')
# def tuesday(request):
#     return HttpResponse("Тоже что и в понедельник")
dic_week_day = {'monday': 'Понедельник!',
                'tuesday': 'Вторник!',
                'wednesday': 'Среда!',
                'thursday': 'Четверг!',
                'friday': 'Пятница!',
                'saturday': 'Суббота!',
                'sunday': 'Воскресенье!',}

def get_info_about_week_days(request, days_week):
    context = {
        'dic_week_day':dic_week_day,
        'days_week':days_week,
    }
    return render(request, 'week_days/greeting.html', context=context)
def get_info_about_week_days_number(request, days_week):
    days=list(dic_week_day)
    if 1<=days_week<=7:
        name_day=days[days_week-1]
        redirect_url = reverse('week_days-name', args=[name_day])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неверный номер дня - {days_week}")



