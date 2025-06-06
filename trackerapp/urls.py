from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_job, name='add_job'),
    path('<int:job_id>/add_note/', views.add_note, name='add_note'),
    path('stats/', views.stats, name='stats')
    # path('job-list/', views.job_list, name='job_list')
]
