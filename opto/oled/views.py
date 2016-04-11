from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templates/oled/oled_landing_en.html")
