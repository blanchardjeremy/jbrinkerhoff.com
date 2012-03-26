import flickr_api
from django.conf import settings

flickr_api.set_keys(api_key = settings.FLICKR_KEY, api_secret = settings.FLICKR_SECRET)