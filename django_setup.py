import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings")
django.setup()