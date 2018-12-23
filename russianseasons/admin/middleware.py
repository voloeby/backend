from django.utils import timezone

from russianseasons.models import Profile


class UpdateLastActivityMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), 'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
        if request.user.is_authenticated():
            Profile.objects.filter(user__id=request.user.id) \
                           .update(last_activity=timezone.now())
