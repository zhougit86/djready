from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    # return HttpResponse('<html><title>Django</title></html>')
    return render(request,'home.html')




def hello(request):
    return HttpResponse("hello")