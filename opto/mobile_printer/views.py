from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templates/thermal_printer/mobile_printer/mobile_printer_landing_en.html")
