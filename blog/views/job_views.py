from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..models import Job
from ..models.id_code import IdCode
from ..models.id_code_manager import IdCodeManager


def create_job(request):
    topic = request.POST['job topic']
    requirement = request.POST['job requirement']
    detail = request.POST['job detail']
    link = request.POST['job link']
    if link.strip():
        link = link.strip()
    else:
        link = ""
    job = Job(topic=topic, requirement=requirement, content=detail, link=link, author=request.user, id_code=IdCodeManager.get_new_id())
    job.save()
    return job

def edit_job(request, job):
    job.topic = request.POST['job topic']
    job.requirement = request.POST['job requirement']
    job.content = request.POST['job detail']
    job.save()

@login_required
def apply_job(request, job_id_code):
    job = Job.objects.filter(id_code=job_id_code).first()
    job.candidates.add(request.user)
    job.save()
    messages.success(request, f'Job applied!!')
    return redirect(reverse('blog:blog-detail', args=[job.id_code]))