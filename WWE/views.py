from django.shortcuts import render

# Create your views here.

def Roman_Reigns(request):
    return render(request, 'Roman_Reigns.html')

def John_Cena(request):
    return render(request, 'John_Cena.html')