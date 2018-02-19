from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'(?P<post_id>[0-9]+)/(?P<user_id>[0-9]+)/deletecomment/(?P<comment_id>[0-9]+)$',views.comment_delete),
    url(r'postpage/(?P<post_id>[0-9]+)/(?P<user_id>[0-9]+)/$',views.postPage),
    url(r'^single/$',views.new_comment),
    url(r'^triple/$',views.new_reply), 
    url(r'^double/$',views.comment_delete),
    url(r'^home/$', views.allPosts),
    url(r'^search/$', views.search),


    url(r'^Category/(?P<cat_id>[0-9]+)$',  views.getPostsCat),
    url(r'^ajax/sub/$', views.subscribe),
    url(r'postpage/(?P<post_id>[0-9]+)/(?P<user_id>[0-9]+)/likepost$',views.likePost),
    #url(r'^dislikePost/$', views.dislikePost, name='dislikepost'),   # likepost view at /likepost
    url(r'postpage/(?P<post_id>[0-9]+)/(?P<user_id>[0-9]+)/dislikepost$', views.dislikePost),

    url(r'^admin/', admin.site.urls),
    url(r'^login_form$', views.login_form),
    url(r'^logged_in_only$', views.logged_in_only)
]
