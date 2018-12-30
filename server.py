import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application 

if __name__ == "__main__":

    application = get_wsgi_application()
    call_command('runserver')