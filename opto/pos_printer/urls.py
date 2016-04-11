from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='pos_printer_landing'),
]
