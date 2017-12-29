from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext
from collections import OrderedDict

from models import Overview, PersonalInfo, Education, Job, Accomplishment, Skillset, Skill, JobCategory

def index(request):
    site_name = RequestSite(request).domain
    personal_info = PersonalInfo.objects.all()[:1]
    overview = Overview.objects.all()[:1]
    education = Education.objects.all()
    job_categories = JobCategory.objects.all()
    skill_sets = Skillset.objects.all()

    job_list = OrderedDict([ (jc.name, jc.job_set.all()) for jc in job_categories ])

    return render_to_response('resume/resume.html', {
        'site_name': site_name,
        'personal_info': personal_info,
        'overview' : overview,
        'job_list' : job_list,
        'education' : education,
        'skill_sets' : skill_sets,
 }, context_instance=RequestContext(request))
