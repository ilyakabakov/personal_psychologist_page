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


class PricesPageView(generic.TemplateView):
    template_name = 'personalpage/prices.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = PricesPageContent.objects.all()
        return context


# def prices(request):
#    text_array = Service.objects.all()#.order_by('id')[:6]
#    context = {'array': text_array}
#    return render(request, 'personalpage/prices.html', context)


class ProductPageView(generic.ListView):
    model = Service
    template_name = 'personalpage/price_table.html'
    queryset = Service.objects.all()


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
