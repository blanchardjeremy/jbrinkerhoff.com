from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
import flickr_api
from portfolio.models import Portfolio


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

class InnerView(TemplateView):
    template_name = 'portfolio/inner.html'


    def get_context_data(self, **kwargs):
        context_data = super(InnerView, self).get_context_data(**kwargs)

        portfolio = Portfolio(settings.FLICKR_USER_ID)
        portfolio.setSections(settings.PORTFOLIO_SECTIONS)
        context_data['portfolio'] = portfolio
        return context_data


class FlickrCacheResetView(RedirectView):
    def get_redirect_url(self, **kwargs):

        # Reset the flickr cache
        cache.clear()

        return reverse('inner')