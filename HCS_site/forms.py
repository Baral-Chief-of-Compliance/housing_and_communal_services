from django import forms
from .models import  Comments, Complaint
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ('news','date_of_comment')
        fileds = ('name_of_commenter', 'text_of_comment' )


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        exclude = ('date_of_complaint',)
        fileds = ('address_of_complaint', 'text_of_complaint')
