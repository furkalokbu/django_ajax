from django.contrib import admin
from posts.models import Post, Photo


admin.site.register(Post)
admin.site.register(Photo)