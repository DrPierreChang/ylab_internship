import os
import sys
sys.path.append('/home/bitnami/django_projects/wisdompets')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/django_projects/wisdompets/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wisdompets.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
