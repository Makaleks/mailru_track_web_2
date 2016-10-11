# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('num_comments', models.IntegerField(default=0)),
                ('num_likes', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('content_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-create_date',),
                'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u044b',
            },
        ),
    ]