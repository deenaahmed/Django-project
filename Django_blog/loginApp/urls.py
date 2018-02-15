"""Django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns, include
from django.contrib import admin

# urlpatterns = [
#      #url(r'^admin/', include(admin.site.urls)),
#      url (r'^login/$', 'django.contrib.auth.views.login'),
#  ]




urlpatterns = patterns('',
(r'^$',views.main_page),
(r'^user/(\w+)/$',view.user_page),
(r'^login/$', 'django.contrib.auth.views.login'),
(r'^logout/$',views.logout_page),
(r'^register/$', views.register_page)
)

# urlpatterns = patterns('',(r'^$', main_page),   
#  (r'^user/(\w+)/$', user_page),
#  (r'^login/$', 'django.contrib.auth.views.login'),

#  )