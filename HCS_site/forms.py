from django import forms
from .models import  Comments


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ("name_of_commenter", "text_of_comment")
