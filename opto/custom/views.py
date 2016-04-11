from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templates/custom/custom_landing_en.html")