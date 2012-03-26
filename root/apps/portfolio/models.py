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
#        photosA = photoset.getPhotos(extras=extras)
#
#        for photo in photosA:
#            photo.__dict__.update({'loaded':True})

        args = dict()
        args['extras'] = ','.join(extras)
        photos = call_api(method="flickr.photosets.getPhotos", photoset_id=photoset.id, **args)
#        photos = [p.getPhotoFile(size_label='Square') for p in photos_all]
        return photos['photoset']['photo']

