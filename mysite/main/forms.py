from django.forms import ModelForm, Textarea
from .models import Text


class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = ["text"]
        widgets = {
            "text": Textarea(attrs={
                'class': 'from-control',
                'placeholder': 'Введите текст',
                'rows': '7',
                'style': 'min-width: 100%'
            }),
        }
