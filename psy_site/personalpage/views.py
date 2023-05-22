from django.shortcuts import render, redirect
from django.views import generic

from .forms import NewClientForm
from .models import HomePageContent, AboutPageContent, PricesPageContent, Service, SocialNetworksLinks


class HomePageView(generic.TemplateView):
    template_name = 'personalpage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = HomePageContent.objects.all()
        context['links'] = SocialNetworksLinks.objects.all()
        return context


class AboutPageView(generic.TemplateView):
    template_name = 'personalpage/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = AboutPageContent.objects.all()
        context['links'] = SocialNetworksLinks.objects.all()
        return context


class PricesPageView(generic.TemplateView):
    template_name = 'personalpage/prices.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text1'] = PricesPageContent.objects.all()
        context['text2'] = Service.objects.all()
        context['links'] = SocialNetworksLinks.objects.all()
        return context


""" NEW CLIENT QUERY """


def query(request):
    links = SocialNetworksLinks.objects.all()
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
        'err': err,
        'links': links
    }
    return render(request, 'personalpage/query.html', context)
