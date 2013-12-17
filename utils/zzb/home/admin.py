from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin
from .models import Gititem
# Register your models here.

admin.site.register(Gititem, MarkdownModelAdmin)
