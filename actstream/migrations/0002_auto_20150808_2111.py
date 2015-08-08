# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='data',
        ),
        migrations.AlterField(
            model_name='action',
            name='actor_content_type',
            field=models.ForeignKey(related_name='actor', to='contenttypes.ContentType', null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='actor_object_id',
            field=models.CharField(max_length=255, null=True, db_index=True),
        ),
    ]
