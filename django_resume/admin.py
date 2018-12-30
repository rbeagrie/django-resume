from django.contrib import admin

from .models import Overview, PersonalInfo, Education, Job,\
    Accomplishment, Skillset, Skill, School, Company,\
    JobCategory

class AccomplishmentAdmin(admin.ModelAdmin):
    list_select_related = True
    ordering = ['job__company','order']

class SkillAdmin(admin.ModelAdmin):
    list_select_related = True
    ordering = ['skillset__name','name']

admin.site.register(PersonalInfo)
admin.site.register(Overview)
admin.site.register(Education)
admin.site.register(JobCategory)
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Accomplishment, AccomplishmentAdmin)
admin.site.register(Skillset)
admin.site.register(Skill, SkillAdmin)
admin.site.register(School)
