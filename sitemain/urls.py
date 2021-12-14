from django.contrib import admin
from django.urls import path, include

from sitemain.views import view_homepage, view_resume

urlpatterns = [
    path('', view_homepage , name ='site-home'),
    path('resume', view_resume, name='my-resume')
]