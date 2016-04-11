from braces.views import FormMessagesMixin
from envelope.views import ContactView

from django.utils.translation import ugettext_lazy as _

from .forms import MyContactForm


class MyContactView(FormMessagesMixin, ContactView):
    form_valid_message = _(u"Thank you for your message.")
    form_invalid_message = _(u"There was an error in the contact form.")
    form_class = MyContactForm