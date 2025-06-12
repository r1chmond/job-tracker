from trackerapp.models import Job, Note
from django import template

register = template.Library()


@register.filter
def get_notes(job):
    notes = Note.objects.filter(job=job)
    return notes

@register.filter
def check_class_name(status):
    lowered_status = status.lower()
    if lowered_status == 'not selected':
        return 'rejected'
    return lowered_status

@register.filter
def shorten_url(url):
    shortened = url[:35] + '...'
    return  shortened