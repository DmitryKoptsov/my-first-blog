from django.contrib import admin
from .models import Post, Blog, Comments

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Comments)