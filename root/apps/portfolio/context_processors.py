from django.core.urlresolvers import reverse
from portfolio.models import Quote

def quotes(request):
    quote = Quote.objects.all().order_by('?')[0]
    return {'quote': quote}

def is_home(request):
    return {'is_inner': bool(request.META['PATH_INFO'] == reverse('inner'))}