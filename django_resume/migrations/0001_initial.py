# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
                'db_table': 'accomplishments',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('company_url', models.URLField(verbose_name=b'Company URL')),
                ('company_image', models.CharField(help_text=b'path to company image, local or otherwise', max_length=250, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('summary', models.TextField(blank=True)),
                ('is_current', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('is_current', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-completion_date', '-start_date'],
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Overview',
            },
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('locality', models.CharField(help_text=b'e.g. city such as Boston', max_length=255)),
                ('region', models.CharField(help_text=b'e.g. state such as Massachusetts', max_length=255)),
                ('region_shorthand', models.CharField(help_text=b'e.g. shorthand (abbr), MA for Massachusetts', max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('twitter', models.CharField(help_text=b'Twitter handle', max_length=255, blank=True)),
                ('github', models.CharField(help_text=b'Github username', max_length=255, blank=True)),
                ('blog', models.URLField(help_text=b'URL to a personal blog', max_length=255, blank=True)),
                ('linkedin', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Personal Info',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('school_url', models.URLField(verbose_name=b'School URL')),
                ('education', models.ForeignKey(to='django_resume.Education')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('skill_url', models.URLField(verbose_name=b'Skill URL', blank=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='skillset',
            field=models.ForeignKey(to='django_resume.Skillset'),
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=1, to='django_resume.JobCategory'),
        ),
        migrations.AddField(
            model_name='company',
            name='job',
            field=models.ForeignKey(to='django_resume.Job'),
        ),
        migrations.AddField(
            model_name='accomplishment',
            name='job',
            field=models.ForeignKey(to='django_resume.Job'),
        ),
    ]
