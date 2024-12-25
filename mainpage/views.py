from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')

def geography(request):
    return render(request, 'mainpage/geography.html')

def skills(request):
    return render(request, 'mainpage/skills.html')

def relevance(request):
    return render(request, 'mainpage/relevance.html')

def last_vacancies(request):
    return render(request, 'mainpage/last_vacancies.html')

def statistics(request):
    return render(request, 'mainpage/statistics.html')