from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='contact_page'),
]