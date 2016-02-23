from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.


def index(request):
    year_copyright = datetime.now().strftime('%Y')
    template = loader.get_template('frontend/index_en.html')
    context = {'user': 'anonymous', 'year_copyright': year_copyright}
    return HttpResponse(template.render(context=context, request=request))
