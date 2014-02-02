# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'django_resume_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_resume.Job'])),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('company_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('company_image', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'django_resume', ['Company'])

        # Deleting field 'Job.company_url'
        db.delete_column('jobs', 'company_url')

        # Deleting field 'Job.company'
        db.delete_column('jobs', 'company')

        # Deleting field 'Job.company_image'
        db.delete_column('jobs', 'company_image')

        # Deleting field 'Job.location'
        db.delete_column('jobs', 'location')


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'django_resume_company')

        # Adding field 'Job.company_url'
        db.add_column('jobs', 'company_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Job.company'
        db.add_column('jobs', 'company',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250),
                      keep_default=False)

        # Adding field 'Job.company_image'
        db.add_column('jobs', 'company_image',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)

        # Adding field 'Job.location'
        db.add_column('jobs', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250),
                      keep_default=False)


    models = {
        u'django_resume.accomplishment': {
            'Meta': {'ordering': "['order']", 'object_name': 'Accomplishment', 'db_table': "'accomplishments'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_resume.Job']"}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'django_resume.company': {
            'Meta': {'object_name': 'Company'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'company_image': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'company_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_resume.Job']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'django_resume.education': {
            'Meta': {'object_name': 'Education'},
            'completion_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'django_resume.job': {
            'Meta': {'ordering': "['-completion_date', '-start_date']", 'object_name': 'Job', 'db_table': "'jobs'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['django_resume.JobCategory']"}),
            'completion_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'django_resume.jobcategory': {
            'Meta': {'object_name': 'JobCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'django_resume.overview': {
            'Meta': {'object_name': 'Overview'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'django_resume.personalinfo': {
            'Meta': {'object_name': 'PersonalInfo'},
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region_shorthand': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'django_resume.school': {
            'Meta': {'object_name': 'School'},
            'education': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_resume.Education']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'school_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'django_resume.skill': {
            'Meta': {'ordering': "['id']", 'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'skill_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'skillset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_resume.Skillset']"})
        },
        u'django_resume.skillset': {
            'Meta': {'object_name': 'Skillset'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['django_resume']