from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from basic_app import views
    
    

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', views.register, name = 'register'),
    url(r'^user_login/$', views.user_login, name = 'user_login'),
    url(r'^$', views.index, name = 'index'),
]

# now we've added the urls, we ned to alter the base.html so that it shows 'login' or 'logout' at appropriate time