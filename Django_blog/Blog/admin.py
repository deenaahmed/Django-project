from django.contrib import admin
from Blog.models import Category,Post,Comment,BadWord,Category_Subscribe,Post_Tag,Reply,Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(BadWord)
admin.site.register(Comment)
admin.site.register(Category_Subscribe)
admin.site.register(Tag)
admin.site.register(Post_Tag)
admin.site.register(Reply)

