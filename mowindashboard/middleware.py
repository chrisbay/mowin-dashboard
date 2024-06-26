from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.utils.deprecation import MiddlewareMixin
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):

    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """

    def process_request(self, request):
        
        assert hasattr(request, 'user'), "The Login Required middleware\
 requires authentication middleware to be installed. Edit your\
 MIDDLEWARE_CLASSES setting to insert\
 'django.contrib.auth.middleware.AuthenticationMiddleware'. If that doesn't\
 work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
 'django.core.context_processors.auth'."
        
        path = request.path_info.lstrip('/')
        is_path_landing = path == settings.LANDING_URL.lstrip('/')
        is_authenticated = request.user.is_authenticated
        is_path_exempt = any(m.match(path) for m in EXEMPT_URLS) or is_path_landing

        if not (is_authenticated or is_path_exempt):
            return HttpResponseRedirect(settings.LANDING_URL)
        elif is_authenticated and is_path_landing:
            return HttpResponseRedirect(settings.HOME_URL)

