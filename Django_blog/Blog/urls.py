
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home/$', views.allPosts),
    url(r'^search/$', views.search),
    url(r'^Category/(?P<cat_id>[0-9]+)$',  views.getPostsCat),
    url(r'^ajax/sub/$', views.subscribe),


]
