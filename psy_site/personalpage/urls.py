from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path("", views.index, name="home"),
    path('about', views.AboutPageView.as_view(), name='about'),
    # path("about", views.about, name="about"),
    path('prices', views.PricesPageView.as_view(), name='prices'),
    path("price_table", views.ProductPageView.as_view(), name="price_table"),
    path("query", views.query, name="query"),
]
