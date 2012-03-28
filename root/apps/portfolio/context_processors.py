from portfolio.models import Quote

def quotes(request):
    quote = Quote.objects.all().order_by('?')[0]
    return {'quote': quote}