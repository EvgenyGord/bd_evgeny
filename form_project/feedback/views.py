from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView



class FeedBackViewUpdate(UpdateView):
    model = Feedback
    fields = ['name']
    # form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'


# Create your views here.
# class FeedBackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})




# class FeedBackView(FormView):
#     form_class = FeedbackForm
#     template_name = 'feedback/feedback.html'
#     success_url = '/done'
#
#     def form_valid(self, form):
#         form.save()
#         return super(FeedBackView, self).form_valid(form)

class FeedBackView(CreateView):
    model = Feedback
    #fields = '__all__'
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'



    # def post(self, request):
    #     form = FeedbackForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()
    #         return HttpResponseRedirect('/done')
    #     return render(request, 'feedback/feedback.html', context={'form': form})

class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I.I'
        context['date'] = '23.04.2022'
        return context




class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})

# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['all_feedback'] = Feedback.objects.all()
#         return context

class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'all_feedback' #если этого параметра нет, то будет называться -> object_list


    def get_queryset(self):
        queryset = super().get_queryset()
        # filter_qs = queryset.filter(rating__gt=3)
        # return filter_qs
        return queryset

# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['one_feedback'] = Feedback.objects.get(id=kwargs['id_feedback'])
#         return context

class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    context_object_name = 'one_feedback'



# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
#
# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
# def done(request):
#     return render(request, 'feedback/done.html')
