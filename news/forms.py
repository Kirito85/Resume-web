from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title',"anons",'full_text','date']

        widgets ={
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder':"name of news"
            }),
            "anons": TextInput(attrs={
                'class': "form-control",
                'placeholder': "anons"
            }),
            "full_text": Textarea(attrs={
                'class': "form-control",
                'placeholder': "text"
            }),
            "date": DateTimeInput(attrs={
                'class': "form-control",
                "type": 'datetime-local',
                'placeholder': "date of publication",
            }),
        }