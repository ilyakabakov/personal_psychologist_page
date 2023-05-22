from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('prices', views.PricesPageView.as_view(), name='prices'),
    path("query", views.query, name="query"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
