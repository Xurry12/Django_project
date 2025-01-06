from django.contrib import admin

from mainpage.models import Info, Statistics, Geography, Relevance, Top20, Top20Analytic

# Register your models here.

admin.site.register(Info)
admin.site.register(Statistics)
admin.site.register(Geography)
admin.site.register(Relevance)
admin.site.register(Top20)
admin.site.register(Top20Analytic)