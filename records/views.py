from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page():
    pass

def hello(request):
    return HttpResponse("hello")