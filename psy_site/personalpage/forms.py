from .models import Client
from django.forms import ModelForm, TextInput, Textarea


class NewClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'gmt', 'query']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ваше имя"
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Номер телефона"
            }),
            'gmt': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Часовой пояс или город в котором проживаете"
            }),
            'query': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Напишите ваш запрос"
            }),
        }
