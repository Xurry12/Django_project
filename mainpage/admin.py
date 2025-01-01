from django.contrib import admin

from mainpage.models import Info, Statistics, Geography, Relevance, Top20

# Register your models here.

admin.site.register(Info)
admin.site.register(Statistics)
admin.site.register(Geography)
admin.site.register(Relevance)
admin.site.register(Top20)