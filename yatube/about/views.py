from django.shortcuts import render
from django.views.generic import TemplateView


# from django.views.generic.base import TemplateView
# Create your views here.

class AboutAuthorView(TemplateView):
    template_name ='about/about_author.html'

class AboutTechView(TemplateView):
    template_name ='about/about_tech.html'