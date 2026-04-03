from django.contrib import admin

# Register your models here.
# blog/admin.py

from .models import Post  # Make sure this import exists

# Register your Post model
admin.site.register(Post)