
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from . import views

urlpatterns = [
                  path('', views.HomePageView.as_view(), name='home'),
                  path('about', views.AboutPageView.as_view(), name='about'),
                  path('prices', views.PricesPageView.as_view(), name='prices'),
                  path("query", views.query, name="query"),
                  path('robots.txt/',
                       TemplateView.as_view(template_name='personalpage/robots.txt',
                                            content_type='text/plain')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "personalpage.views.page_not_found_view"

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
