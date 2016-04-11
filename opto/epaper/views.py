from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templates/epaper/epaper_landing_en.html")