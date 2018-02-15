from django.conf.urls import include, url
from django.contrib import admin
from Blog import views



urlpatterns = [
    url(r'^test/',views.test ),
]