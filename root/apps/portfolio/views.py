from django.conf import settings
from django.views.generic import TemplateView
import flickr_api
from portfolio.models import Portfolio

# Create your views here.


class TempView(TemplateView):
    template_name = 'portfolio/temp.html'

    def get_context_data(self, **kwargs):
        context_data = super(TempView, self).get_context_data(**kwargs)

        portfolio = Portfolio(settings.FLICKR_UESR_ID)
        photosets = portfolio.getPhotosets()
        context_data['photos'] = portfolio.getPhotos(photosets[1])
        return context_data


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

class InnerView(TemplateView):
    template_name = 'portfolio/inner.html'