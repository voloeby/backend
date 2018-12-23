from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from russianseasons.models import Profile

class CheckUserActivityMiddleware(MiddlewareMixin):
	def process_request(self, request):
		if request.user.is_authenticated:
			request.user.profile.last_activity = timezone.now()
			request.user.save()
		print(request.user.profile.last_activity)
		return None
