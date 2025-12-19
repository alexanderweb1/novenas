from django.shortcuts import render
from django.views import View
# Create your views here.

def home(request):
    return render(request, 'home.html')

def virgenC(request):
    return render(request, 'virgenC.html')

def divinoN(request):
    return render(request, 'divinoN.html')

def novena_diaN(request, novena, dia):
    return render(request, f'DiasNino/Dia{dia}.html', {'novena': novena, 'dia': dia})

def novena_diaC(request, novena, dia):
    return render(request, f'DiasCisne/Dia{dia}n.html', {'novena': novena, 'dia': dia})