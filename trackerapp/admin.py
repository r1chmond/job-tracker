from django.contrib import admin
from trackerapp.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'url', 'location')

admin.site.register(Job, JobAdmin)