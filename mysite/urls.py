"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mysite import views
from records import views as recviews


urlpatterns = [
    url(r'^$',recviews.home_page,name='home'),
    url(r'^lists/the-only-list/',recviews.view_list,name='view_list'),
    url(r'^lists/new$', recviews.new_list, name='new_list'),
    url(r'^admin/', admin.site.urls),
    # url(r'^hello/(?P<offset>\d?)/$',views.hello,{"temp":"temp.html","GET":views.get_view}),
    # url(r'record/',include('records.urls')),
    # url(r'^network/$',views.network),
]
