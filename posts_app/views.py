from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'paginas/homebase.html')
    
def servicos(request):
    return render(request,'paginas/servicos.html')
    
