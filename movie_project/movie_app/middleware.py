from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache

class RequestCounterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not cache.get('request_count'):
            cache.set('request_count', 0)
        cache.incr('request_count', 1)
