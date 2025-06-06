from django.db import models
from django.core.validators import RegexValidator

class Status(models.TextChoices):
    BOOKMARKED = 'Bookmarked'
    APPLIED = 'Applied'
    INTERVIEWING = 'Interviewing'
    NOT_SELECTED = 'Not Selected'
    OFFER = 'Offer'

class Job(models.Model):
    title = models.CharField(max_length=500, blank=False, 
                             validators=[RegexValidator(
                               regex = r'^[A-Za-z\s]+$',
                               message = 'title must only be alphabets'  
                             )])
    company = models.CharField(max_length=500, 
                               blank=False,
                               validators=[
                                   RegexValidator(
                                       regex = r'^[A-Za-z0-9\s]+$',
                                       message= 'company name cannot include symbols'
                                   )
                               ])
    url = models.URLField(max_length=500, blank=False,)
    location = models.CharField(max_length=500, 
                                blank=False,
                                validators=[RegexValidator(
                               regex = r'^[A-Za-z\s]+$',
                               message = 'location must only be alphabets')])
    status = models.CharField(max_length=20, blank=False)
    description = models.TextField()
    date_time_added= models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_time_added',)

class Note(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    note = models.TextField()
    date_time_added = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ('-date_time_added',)



