from django.contrib import admin

from .models import product, Comment

admin.site.register(product)
admin.site.register(Comment)
