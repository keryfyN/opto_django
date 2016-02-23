from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"templates/tft/tft_displays_landing_en.html")
