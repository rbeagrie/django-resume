# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Overview'
        db.create_table(u'django_resume_overview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'django_resume', ['Overview'])

        # Adding model 'PersonalInfo'
        db.create_table(u'django_resume_personalinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region_shorthand', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'django_resume', ['PersonalInfo'])

        # Adding model 'Education'
        db.create_table(u'django_resume_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('school_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('completion_date', self.gf('django.db.models.fields.DateField')()),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('is_current', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'django_resume', ['Education'])

        # Adding model 'Job'
        db.create_table('jobs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('company_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('completion_date', self.gf('django.db.models.fields.DateField')()),
            ('is_current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('company_image', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'django_resume', ['Job'])

        # Adding model 'Accomplishment'
        db.create_table('accomplishments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_resume.Job'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'django_resume', ['Accomplishment'])

        # Adding model 'Skillset'
        db.create_table(u'django_resume_skillset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'django_resume', ['Skillset'])

        # Adding model 'Skill'
        db.create_table(u'django_resume_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('skill_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('skillset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_resume.Skillset'])),
        ))
        db.send_create_signal(u'django_resume', ['Skill'])


    def backwards(self, orm):
        # Deleting model 'Overview'
        db.delete_table(u'django_resume_overview')

        # Deleting model 'PersonalInfo'
        db.delete_table(u'django_resume_personalinfo')

        # Deleting model 'Education'
        db.delete_table(u'django_resume_education')

        # Deleting model 'Job'
        db.delete_table('jobs')

        # Deleting model 'Accomplishment'
        db.delete_table('accomplishments')

        # Deleting model 'Skillset'
        db.delete_table(u'django_resume_skillset')

        # Deleting model 'Skill'
        db.delete_table(u'django_resume_skill')


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region_shorthand': ('django.db.models.fields.CharField', [], {'max_length': '64'})
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