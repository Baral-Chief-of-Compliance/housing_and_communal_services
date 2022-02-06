from django import forms
from .models import  Comments
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ('news',)
        fileds = ['date_of_news', 'name_of_commenter', 'text_of_comment']
        widgets = {
            "name_of_commenter": TextInput(attrs={
                'placeholder': 'Ваше имя'
            }),
            "text_of_comment": TextInput(attrs={
                'placeholder': 'Текст комментария'
            }),
        }
