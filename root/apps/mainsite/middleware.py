from django.http import HttpResponseRedirect

class RemoveWWWRedirectMiddleware(object):
    def process_request(self, request):
        host = request.META['HTTP_HOST']
        if host.startswith('www.'):
            host = host.replace('www.', '', 1)
            # TODO: Could build up the whole path with build_absolute_uri so nothing is lost in the redirect
            return HttpResponseRedirect('http://%s' % host)
