from django.shortcuts import render

# Create your views here.


def my_information(request):

    return render(request, 'blog/information.html')

def my_education(request):
    return render(request, 'blog/education.html')

def my_programming(request):
    return  render(request, 'blog/programming.html')

