from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templates/thermal_printer/panel_printer/panel_printer_landing_en.html")
