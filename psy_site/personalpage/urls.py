from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('prices', views.prices, name='prices'),
    path("query", views.query, name="query"),
]
