from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
import flickr_api
from flickr_api.method_call import call_api

# Enable caching
from django.core.cache import cache
flickr_api.enable_cache(cache)


class Portfolio(object):

    def __init__(self, user_id):
        """
        sections is a dictionary with keys as a title of the section and values as the flickr set ID for items to display in that section
        """
#        self.user = flickr_api.Person(id=user_id) # Not currently used
        self._sections = []

    def setSections(self, section_settings):
        for title, set_id in section_settings.iteritems():
            self._sections.append(PortfolioSection(title, set_id))

    def getSections(self):
        return self._sections


class PortfolioSection(object):

    def __init__(self, title, set_id):
        self.title = title
        self.slug = slugify(title)
        self.set_id = set_id
        self.photoset = flickr_api.Photoset(id=set_id)

    def getPhotos(self):
        extras = ['url_sq', 'url_s', 'url_t', 'url_m', 'url_o', 'description']
        return self.photoset.getPhotos(extras=extras)
