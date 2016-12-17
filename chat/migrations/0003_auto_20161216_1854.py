# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20161214_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='sentence',
            name='conversation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chat.Conversation'),
        ),
    ]
