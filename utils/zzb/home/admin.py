from django.contrib import admin

# from django_markdown.admin import MarkdownModelAdmin
from django.db import models
from .forms import GititemForm
from .models import Gititem
# Register your models here.

# class MarkdownModelAdmin(models.ModelAdmin):
# 	formfield_overrides = {
# 		models.TextField: {'widget': Gititem},
# 	}
# 	form = GititemForm
	
# admin.site.register(Gititem, MarkdownModelAdmin)
