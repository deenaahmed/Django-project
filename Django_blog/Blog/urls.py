
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home/$', views.allPosts),
    url(r'^search/$', views.search),
    url(r'^likepost/$', views.likePost, name='likepost'),   # likepost view at /likepost
    url(r'^dislikePost/$', views.dislikePost, name='dislikepost'),   # likepost view at /likepost


]
