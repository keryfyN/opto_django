from django.apps import AppConfig
from flask_wtf.csrf import CsrfProtect

class FrontendConfig(AppConfig):
    name = 'frontend'


