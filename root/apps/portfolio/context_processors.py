from django.conf import settings
from django.core.urlresolvers import reverse
from portfolio.models import Quote

def quotes(request):
    quote = Quote.objects.all().order_by('?')[0]
    return {'quote': quote}

def base(request):
    return {
        'is_inner': bool(request.META['PATH_INFO'] == reverse('inner')),
        'USER_EMAIL': settings.USER_EMAIL,
        'WUFOO_FORM_URL': settings.WUFOO_FORM_URL,
        'WUFOO_FORM_KEY': settings.WUFOO_FORM_KEY,
    }