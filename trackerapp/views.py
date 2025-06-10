from django.shortcuts import render,redirect, get_object_or_404
from trackerapp.forms import JobForm, NoteForm
from trackerapp.models import Job, Note, Status
import logging
from django.contrib import messages
from collections import Counter

logger = logging.getLogger(__name__)



def home(request):
    job_form = JobForm() 
    note_form = NoteForm()
    query = request.GET.get('search-input')
    if query:
        jobs = Job.objects.filter(title__icontains=query)
    else:
        jobs = Job.objects.all()
    
    context = {
        'note_form': note_form,
        'job_form': job_form,
        'jobs': jobs,
        'query': query,
    }
    return render(request, 'home.html',context)

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Form is invalid')
    return redirect('home')

def add_note(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['job'] = job.pk
        form = NoteForm(form_data)
        if form.is_valid():
            form.save()
    return redirect('home')
            
             

def stats(request):
    total_jobs = Job.objects.count()
    bookmarked_jobs = Job.objects.filter(status=Status.BOOKMARKED).count()
    applied_jobs = Job.objects.filter(status=Status.APPLIED).count()
    interviewing_jobs = Job.objects.filter(status=Status.INTERVIEWING).count() 
    offer_jobs = Job.objects.filter(status=Status.OFFER).count() 
    rejected_jobs = Job.objects.filter(status=Status.NOT_SELECTED).count()

    context = {
        'total_jobs': total_jobs, 
        'applied_jobs': applied_jobs,
        'bookmarked_jobs': bookmarked_jobs,
        'interviewing_jobs': interviewing_jobs,
        'offer_jobs': offer_jobs,
        'rejected_jobs': rejected_jobs
    }

    return render(request, 'stats.html', context)
    


def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Form is invalid')
    return redirect('home')

def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['job'] = note.job
        form = NoteForm(form_data, instance=note)
        if form.is_valid():
            form.save()
    return redirect('home')
            

def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return redirect('home')

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('home')