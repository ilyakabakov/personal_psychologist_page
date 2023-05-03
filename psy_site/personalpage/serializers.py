from rest_framework.serializers import ModelSerializer

from personalpage.models import HomePageContent


class TextContainerSerializer(ModelSerializer):
    class Meta:
        model = HomePageContent
        fields = ('name', 'title', 'text')
