from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content','order' ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'order': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.NumberInput(attrs={'class':'form-control'}),
        }