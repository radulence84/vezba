import os
import django
from django.conf import settings

# Set up Django before any tests are run
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vezba.settings")
django.setup()