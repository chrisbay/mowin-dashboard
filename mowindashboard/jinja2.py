from django.contrib.staticfiles.storage import staticfiles_storage
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
    })
    return env
