from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    # return HttpResponse('<html><title>Django</title></html>')
    if request.method=='POST':
        return render(request,'home.html',{'new_item_text':request.POST.get('item_text','')})
    return render(request,'home.html')




def hello(request):
    return HttpResponse("hello")