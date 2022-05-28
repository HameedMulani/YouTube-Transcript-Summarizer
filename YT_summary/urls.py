from django import urls
from django.contrib import admin 
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import include, re_path


urlpatterns = [
    
    #format with nltk(FINAL)
    re_path(r'^$', views.srch),
    re_path(r'^Get_sum', views.get_sum),

    
]