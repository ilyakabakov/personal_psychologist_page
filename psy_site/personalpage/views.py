from django.shortcuts import render, redirect
from django.views import generic

from .forms import NewClientForm
from .models import HomePageContent, AboutPageContent, PricesPageContent, Service


# def index(request):
#     text_container = HomePageContent.objects.order_by('id')[:1]
#     context = {'title': 'Главная страница сайта',
#                'text': text_container}
#     return render(request, 'personalpage/index.html', context)


class HomePageView(generic.TemplateView):
    template_name = 'personalpage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = HomePageContent.objects.all()
        return context


class AboutPageView(generic.TemplateView):
    template_name = 'personalpage/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = AboutPageContent.objects.all()
        return context


def prices(request):
    text_array = PricesPageContent.objects.all()
    text_array2 = Service.objects.all()
    context = {'text1': text_array, 'text2': text_array2}
    return render(request, 'personalpage/prices.html', context=context)


""" NEW CLIENT QUERY """


def query(request):
    err = ''
    if request.method == "POST":
        form = NewClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            err = 'Вы ввели некорректное значение'

    form = NewClientForm()
    context = {
        'form': form,
        'err': err
    }
    return render(request, 'personalpage/query.html', context)
