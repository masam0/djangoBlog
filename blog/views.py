from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  return HttpResponse("This will be the index of my blog")
