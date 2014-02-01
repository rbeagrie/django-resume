# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PersonalInfo.github'
        db.add_column(u'django_resume_personalinfo', 'github',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PersonalInfo.github'
        db.delete_column(u'django_resume_personalinfo', 'github')


    models = {
        u'django_resume.accomplishment': {
            'Meta': {'ordering': "['order']", 'object_name': 'Accomplishment', 'db_table': "'accomplishments'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_resume.Job']"}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'django_resume.education': {
            'Meta': {'object_name': 'Education'},
            'completion_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'school_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {})
        },
        u'django_resume.job': {
            'Meta': {'ordering': "['-completion_date', '-start_date']", 'object_name': 'Job', 'db_table': "'jobs'"},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'company_image': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'company_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'completion_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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