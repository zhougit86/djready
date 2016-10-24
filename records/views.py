from django.shortcuts import render,redirect
from django.http import HttpResponse

from models import Item

# Create your views here.

def home_page(request):
    # return HttpResponse('<html><title>Django</title></html>')
    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    # else:
    #     new_item_text = ''
    # return render(request, 'home.html', {
    #     'new_item_text': new_item_text,
    # })

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    return render(request, 'home.html',{'items':Item.objects.all()})




def hello(request):
    return HttpResponse("hello")