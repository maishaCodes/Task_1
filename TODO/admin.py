from django.contrib import admin

# Register your models here.

from .models import TODO  #------------3RD

admin.site.register(TODO)