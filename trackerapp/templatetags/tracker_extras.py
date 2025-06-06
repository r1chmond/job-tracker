from trackerapp.models import Job, Note
from django import template

register = template.Library()


@register.filter
def get_notes(job):
    notes = Note.objects.filter(job=job)
    return notes