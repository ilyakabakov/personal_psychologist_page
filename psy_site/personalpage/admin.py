from django.contrib import admin
from .models import Client, HomePageContent, AboutPageContent, PricesPageContent, Service, SocialNetworksLinks

admin.site.register(Client)
admin.site.register(HomePageContent)
admin.site.register(AboutPageContent)
admin.site.register(PricesPageContent)
admin.site.register(Service)
admin.site.register(SocialNetworksLinks)

