import time
from datetime import datetime
from django.db import models 

class Overview(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Overview"

    def __unicode__(self):
        return self.text[0:40] + '...'

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, help_text="e.g. city such as Boston")
    region = models.CharField(max_length=255, help_text="e.g. state such as Massachusetts")
    region_shorthand = models.CharField(max_length=64, help_text="e.g. shorthand (abbr), MA for Massachusetts")
    email = models.EmailField()
    twitter = models.CharField(max_length=255, help_text="Twitter handle", blank=True)
    github = models.CharField(max_length=255, help_text="Github username", blank=True)
    blog = models.URLField(max_length=255, help_text="URL to a personal blog", blank=True)
    linkedin = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = "Personal Info"
    
    def full_name(self):
        return " ".join([self.first_name, self.last_name])
    
    def __unicode__(self):
        return self.full_name()

class Education(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    completion_date = models.DateField()
    summary = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Education"

    def edu_date_range(self):
        return ''.join(['(', self.formatted_start_date(), 
            '-', self.formatted_end_date(), ')'])

    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.completion_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.completion_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.name, self.edu_date_range()])

    def summary_as_list(self):
        return self.summary.split('|')

    def has_summary_items(self):
        if self.summary == "":
            return False
        else:
            return True

class School(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    school_url = models.URLField('School URL')
    education = models.ForeignKey('Education', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class JobCategory(models.Model):
    name = models.CharField(max_length=250)
    order = models.IntegerField(default=0)

    @staticmethod
    def get_other():
        return JobCategory.objects.get_or_create(name='Other')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order']

class Job(models.Model):

    category = models.ForeignKey(JobCategory, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    completion_date = models.DateField()
    is_current = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)

    class Meta:
        db_table = 'jobs'
        ordering = ['-completion_date','-start_date']

    def job_date_range(self):
        return ''.join(['(', self.formatted_start_date(),'-', 
            self.formatted_end_date(), ')'])
    
    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.completion_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")
        
    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.completion_date.strftime("%b %Y")

    def __unicode__(self):
        return ': '.join([self.title, self.job_date_range()])

    def end_year(self):
        if not self.is_current:
            return self.completion_date.year
        else:
            return datetime.now().year

class Company(models.Model):

    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    company = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    company_url = models.URLField('Company URL')
    company_image = models.CharField(max_length=250, blank=True, 
        help_text='path to company image, local or otherwise')

    def __unicode__(self):
        return self.company

class Accomplishment(models.Model):
    description = models.TextField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        db_table = 'accomplishments'
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.job.title, '-', self.description[0:50], '...'])

class Skillset(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name =  models.CharField(max_length=250)
    skill_url = models.URLField('Skill URL', blank=True)
    skillset = models.ForeignKey(Skillset, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return ''.join([self.skillset.name, '-', self.name])
