# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_googlemap', '0003_auto_20160825_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='googlemap',
            name='template',
            field=models.CharField(default='djangocms_googlemap/googlemap.html', max_length=255, verbose_name=b'Template', choices=[('djangocms_googlemap/googlemap.html', 'Default'), ('djangocms_googlemap/footer.html', 'Footer')]),
        ),
    ]
