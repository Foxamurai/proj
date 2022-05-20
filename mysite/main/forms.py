from django import forms

from .models import Text


class TextForm(forms.Form):
    text = forms.CharField(
        label='Текст',
        widget=forms.Textarea(
                attrs={
                    'class': 'from-control',
                    'placeholder': 'Введите текст',
                    'rows': '7',
                    'style': 'min-width: 100%'
                })

    )


class FileForm(forms.Form):
    file = forms.FileField(
        label='Файл',
        widget=forms.FileInput(attrs={'accept': 'text/plain'})
    )


class AudioForm(forms.Form):
    file = forms.FileField(
        label='Файл',
        # widget=forms.FileInput(attrs={'accept': 'text/plain'})
    )