# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration( migrations.Migration ) :
    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name = 'question',
            old_name = 'question_test',
            new_name = 'question_text',
        ),
    ]
