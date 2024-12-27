from django.shortcuts import render
from matplotlib.style.core import context

from ulearnProject.parsing import get_vacs
from .models import Info, Statistics2, Statistics  # Analytics, AnalyticsStatistic


# Create your views here.

def index(request):
    context = {
         'info':Info.objects.all()
    }

    return render(request, 'mainpage/index.html', context)

def geography(request):
    return render(request, 'mainpage/geography.html')

def skills(request):
    return render(request, 'mainpage/skills.html')

def relevance(request):
    return render(request, 'mainpage/relevance.html')

def last_vacancies(request):
    vac = get_vacs()
    return render(request, 'mainpage/last_vacancies.html', vac)

def statistics(request):
    context = {
        'info': Statistics.objects.all()
    }
    return render(request, 'mainpage/statistics.html', context)