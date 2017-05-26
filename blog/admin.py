from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from .models import Post,Tag
from pagedown.widgets import AdminPagedownWidget


class Entryadmin(admin.ModelAdmin):
    list_display = ("title","create")
    prepopulated_fields = {"slug":("title",)}
    formfield_overrides = {
        models.TextField:{'widget':AdminPagedownWidget},
    }
admin.site.register(Post,Entryadmin)
admin.site.register(Tag)
