from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MainContent

admin.site.register(MainContent)

from django.contrib import admin
from .models import Subcontent, Comment

admin.site.register(Subcontent)
admin.site.register(Comment)
