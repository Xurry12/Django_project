from django.shortcuts import render
from matplotlib.style.core import context
import json

from ulearnProject.parsing import get_vacs
from .models import Info, Statistics, Geography, Top20, Relevance, Top20Analytic
# Create your views here.

def index(request):
    context = {
            'info': Info.objects.all(),
        }
    return render(request, 'mainpage/index.html', context)

def geography(request):
    context = {
        'geo': Geography.objects.all()
    }
    return render(request, 'mainpage/geography.html', context)

def skills(request):
    years = range(2015, 2025)
    top20_entries = list(Top20Analytic.objects.values('year', 'table', 'image'))  # Получаем только необходимые поля
    return render(request, 'mainpage/skills.html', {
        'years': years,
        'top20_entries': json.dumps(top20_entries),
    })

def relevance(request):
    context = {
        'info':Relevance.objects.all()
    }
    return render(request, 'mainpage/relevance.html', context)

def last_vacancies(request):
    vac = get_vacs()
    return render(request, 'mainpage/last_vacancies.html', vac)

def statistics(request):
    years = range(2015, 2025)
    top20_entries = list(Top20.objects.values('year', 'table', 'image'))
    context = {
        'info':Statistics.objects.all(),
        'years':years,
        'top20_entries':top20_entries
    }
    return render(request, 'mainpage/statistics.html',  context)