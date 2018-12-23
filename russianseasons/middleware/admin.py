
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from django.http import Http404


class CheckUserActivityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin/'):
            if request.user:
                if request.user.is_authenticated:
                    if request.user.is_active:
                        pass
                    else:
                        raise Http404
                else:
                    raise Http404
            else:
                raise Http404
        if request.user:
            if request.user.is_authenticated:
                request.user.profile.last_activity = timezone.now()
                request.user.save()
        return None
