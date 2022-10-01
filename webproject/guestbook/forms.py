from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    author_name = forms.CharField(
        max_length = 100,
        required = True,
        label = 'Имя автора записи',
        widget=widgets.TextInput(attrs={'class': 'form-control'})    
    )
    author_email = forms.EmailField(
        max_length = 100,
        required = True,
        label = 'Почта автора записи',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    textrec = forms.CharField(
        max_length = 600,
        required = True,
        label = 'Текст записи',
        widget = widgets.Textarea(attrs={'class': 'form-control', 'style': 'height:150px'})
    )