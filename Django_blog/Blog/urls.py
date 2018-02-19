from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^single/$',views.new_comment),
    url(r'^triple/$',views.new_reply), 
    url(r'^double/$',views.comment_delete),
    url(r'^home/$', views.allPosts),
    url(r'^search/$', views.search),
    url(r'^Category/(?P<cat_id>[0-9]+)$',  views.getPostsCat),
    url(r'^ajax/sub/$', views.subscribe),
    url(r'^Post/(?P<post_id>[0-9]+)$',  views.postPage),

    url(r'^Tag/(?P<tag_id>[0-9]+)$',  views.getPostsTag),

