from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='lcd_landing'),
    url(r'^graphic$', views.lcd_graphic, name='lcd_graphic'),
    url(r'^segment$', views.lcd_segment, name='lcd_segment'),
]