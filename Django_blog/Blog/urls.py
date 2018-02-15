from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^postpage/1$',views.postPage),
    url(r'postpage/(?P<post_id>[0-9]+)$',views.postPage),
    url(r'postpage/(?P<post_id>[0-9]+)/(?P<user_id>[0-9]+)$',views.new_comment),

]

