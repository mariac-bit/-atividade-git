from django.shortcuts import render

# Create your views here.
def funcao(request):
    return render (request, 'maria.html')

def cristina(request):
    return render(request, 'cristina.html')