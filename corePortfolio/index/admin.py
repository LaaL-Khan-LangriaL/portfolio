from django.contrib import admin
from index.models import hello

# Register your models here.


class HomeIndex(admin.ModelAdmin):
    pass


admin.site.register(hello, HomeIndex)