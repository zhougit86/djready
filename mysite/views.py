from django.http import HttpResponse
from django.template import loader,Context
import datetime
import json

def get_view(request,*args,**kwargs):
    temp=kwargs.pop("temp")
    offset=kwargs.pop("offset")
    now = datetime.datetime.now() + datetime.timedelta(hours=int(offset))
    t = loader.get_template(temp)
    c = Context({
        "time": now,
        "seasonlist": ["spring", "summer", "autumn", "winter"],
        'ip_address': request.META['REMOTE_ADDR'],
    })
    print request.COOKIES["test"]
    # seasonlist=["spring", "summer", "autumn", "winter"]
    # return HttpResponse(json.dumps(seasonlist))
    response= HttpResponse(t.render(c))
    response.set_cookie("test","test")
    return response

def hello(request,*args,**kwargs):
    GET=kwargs.pop("GET",None)
    if request.method == "GET" and GET is not None:
        return GET(request,*args,**kwargs)
