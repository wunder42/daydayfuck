from forms import TForm
from django.contrib import admin


class TModelAdmin(admin.ModelAdmin):
    form = TForm   

admin.site.register(FooModel, TModelAdmin)