from django.contrib import admin
from .models import Content
@admin.register(Content)
class contentAdmin(admin.ModelAdmin):
    list_display=('sector','topic','region','country')


