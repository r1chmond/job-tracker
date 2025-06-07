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
            return redirect('home')
        else:
            messages.error(request, 'Form is invalid')
    else:
        form = JobForm()
        
    return render(request, "home.html", {'job_form': form})

def add_note(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['job'] = job.pk
        form = NoteForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Form in invalid')
    else:
        form = NoteForm()
    return render(request, 'home.html', {'note_form': form, 'cur_job': job})
            
             

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
    

    