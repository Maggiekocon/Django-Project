from django import forms
from .models import Post

class PostForm(forms.ModelForm): #this will just turn your current model into a form
    class Meta():
        model = Post # tells you which model 
        fields = ['title','author','body']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),

            'author': forms.TextInput(attrs={'class': 'form-control'}),

            'body': forms.Textarea(attrs={'class': 'form-control'})

        }