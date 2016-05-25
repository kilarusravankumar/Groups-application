from django.contrib import admin
from posts.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=['__unicode__','timestamp','updated']
    list_filter=['updated','timestamp','title']
    search_fields=['title','content']
    class Meta:
        model=Post
admin.site.register(Post,PostAdmin)