from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_job, name='add_job'),
    path('<int:job_id>/add_note/', views.add_note, name='add_note'),
    path('stats/', views.stats, name='stats'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job')

]
