# Resume App URLs file
from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='resume_home'),
]
