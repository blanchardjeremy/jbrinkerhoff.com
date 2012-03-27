from django.db import models
from cache_utils.decorators import cached
import flickr_api
from flickr_api.method_call import call_api

# Create your models here.


class Portfolio(object):

    def __init__(self, user_id):
        self.user = flickr_api.Person(id=user_id)

    def getPhotosets(self):
        photosets = self.user.getPhotosets()
        return photosets

    def getPhotos(self, photoset):
        extras = ['url_sq', 'url_s', 'url_t', 'url_m', 'url_o']
        return photoset.getPhotos(extras = extras)
