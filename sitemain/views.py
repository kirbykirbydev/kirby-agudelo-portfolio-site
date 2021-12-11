from django.shortcuts import render
from django.http import HttpResponseNotFound


def view_homepage(request):

  return render( request, 'sitehome.html' )