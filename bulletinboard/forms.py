from django import forms
from .models import Bulletinboard, Comment
from froala_editor.widgets import FroalaEditor

class PostForm(forms.ModelForm):
    class Meta:
        model = Bulletinboard
        fields = ['title', 'text','writer','secret']
        widgets = {
            'writer':forms.TextInput(),
            'secret':forms.CheckboxInput(),
            'text': FroalaEditor(),
            'title': forms.TextInput(
                attrs={
                    'style': 'height: 30px; margin-bottom:15px; width:300px;',
                    'autocomplete': 'off'
                }
            )
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text','writer']
        widgets = {
            'writer':forms.TextInput(                
                attrs={
                    'style': 'height: 30px; margin-bottom:15px; width:300px;',
                    'autocomplete': 'off',
                    'class': 'form-control',
                }),
            'text': FroalaEditor()
        }