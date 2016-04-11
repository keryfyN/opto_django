from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templates/lcd/lcd_landing_en.html")

def lcd_graphic(request):
    return render(request, "templates/lcd/graphic/lcd_graphic_landing_en.html")

def lcd_segment(request):
    return render(request, "templates/lcd/segment/lcd_segment_landing_en.html")