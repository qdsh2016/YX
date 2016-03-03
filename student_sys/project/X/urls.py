"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'start', views.start,name='start'),
	url(r'login', views.login,name='login'),
	url(r'signin', views.signin,name='signin'),	
    url(r'ok_insign', views.signin_ok,name='signin_ok'),

    url(r'search', views.search,name='search'),    
    url(r'student', views.student,name='student'),    
    url(r'score', views.score,name='score'),    
    url(r'delete', views.delete,name='delete'),  
    url(r'yyy', views.yyy,name='ok_add'), 
    url(r'add', views.add,name='add'),  
    url(r'id_check', views.id_check,name='id_check'), 
    url(r'update', views.update,name='update'),  
    url(r'kkk', views.ko_update,name='ko_update'),  
    
]
