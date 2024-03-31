import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_spoken_word.settings')

application = get_asgi_application()
