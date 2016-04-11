"""opto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tft/', include('tft.urls')),
    url(r'^oled/', include('oled.urls')),
    url(r'^epaper/', include('epaper.urls')),
    url(r'^custom/', include('custom.urls')),
    url(r'^panel_printer/', include('panel_printer.urls')),
    url(r'^mobile_printer/', include('mobile_printer.urls')),
    url(r'^pos_printer/', include('pos_printer.urls')),
    url(r'^contact/', include('envelope.urls')),
    url(r'^', include('frontend.urls')),
    url(r'^lcd/', include('lcd.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
