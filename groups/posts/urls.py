
from django.conf.urls import url,include
from django.contrib import admin
from .views import (posts_list,
                   posts_create,
                   posts_delete,
                   posts_detail,
                   posts_update,)



urlpatterns = [
    
    url(r'^$',posts_list),
    url(r'^create/',posts_create),
    url(r'^delete/',posts_delete),
    url(r'^(?P<id>\d+)$',posts_detail,name='post_detail'),
    url(r'^(?P<id>\d+)/edit/$',posts_update,name='update'),
    
]
