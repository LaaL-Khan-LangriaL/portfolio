from django.contrib import admin
from blog.models import *
# Register your models here.


class Blog(admin.ModelAdmin):
    pass


admin.site.register(add_Review, Blog),
