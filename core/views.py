""" Creando Vistas basadas en clases"""
from turtle import title
from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':' Mi Super Playground'})

class SampleView(TemplateView):
    template_name = 'core/sample.html'