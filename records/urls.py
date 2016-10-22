from django.conf.urls import url,include
# from django.contrib import admin
from records import views


urlpatterns = [
    url(r'^hello/$',views.hello)
]