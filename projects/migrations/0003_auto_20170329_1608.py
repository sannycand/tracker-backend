# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170313_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='DraftProjectMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=225)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='log',
            name='description',
        ),
        migrations.AlterUniqueTogether(
            name='draftprojectmember',
            unique_together=set([('email', 'project')]),
        ),
    ]