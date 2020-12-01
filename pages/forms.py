from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'formcontrol', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'formcontrol'}),
            'order': forms.NumberInput(attrs={'class':'formcontrol', 'placeholder':'Indique número de orden'}),
        }
        labels ={
            'title':'', 'order':''
        }