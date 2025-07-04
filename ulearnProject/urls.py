"""ulearnProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mainpage.views import index, geography, skills, relevance, last_vacancies,statistics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('geograpy', geography, name='geography'),
    path('skills', skills, name='skills'),
    path('relevance', relevance, name='relevance'),
    path('last_vacancies', last_vacancies, name='last_vacancies'),
    path('statistics', statistics, name='statistics'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
