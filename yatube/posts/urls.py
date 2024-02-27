from django.urls import path
from django.urls.converters import register_converter

from . import views, converters

register_converter(converters.My_slug, type_name='myslug')
app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('group/<myslug:slug>', views.group_posts, name='group_list'),

]
