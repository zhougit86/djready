from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from models import Item,List

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

    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list/')

    return render(request, 'home.html')

def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
        # Item.objects.create(text=request.POST['item_text'], list=list_)
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"
    # items=Item.objects.filter(list=list_)
    return render(request,'list.html',{'list':list_,'error':error})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'],list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)      #you have to define the reverse in the model to use this kind of expression

# def add_item(request,list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect('/lists/%d/' % (list_.id,))

def hello(request):
    return HttpResponse("hello")