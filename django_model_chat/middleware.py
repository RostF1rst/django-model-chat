from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class RestrictAccessToAdminPageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith(reverse('admin:index')):
            if not (request.user.is_authenticated or request.user.is_staff):
                raise PermissionDenied()
