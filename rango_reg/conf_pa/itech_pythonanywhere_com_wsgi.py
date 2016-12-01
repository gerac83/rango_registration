import os
import sys

# Add your project's directory the PYTHONPATH
path = '/home/itech/rango_registration/rango_reg/'
if path not in sys.path:
    sys.path.append(path)

# Move to the project directory
os.chdir(path)

# Tell Django where the settings.py module is located
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rango_reg.settings')

# Import your Django project's configuration
import django
django.setup()

# Import the Django WSGI to handle any requests
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
