from django.contrib import admin

from django.contrib import admin
from .models import CollegeDocument

# Tell the admin dashboard to manage this table
admin.site.register(CollegeDocument)
